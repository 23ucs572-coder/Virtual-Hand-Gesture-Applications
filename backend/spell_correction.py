"""Suggestion-only English spell checking for TrOCR output."""

import csv
import re
from pathlib import Path

try:
    from spellchecker import SpellChecker
except ImportError:  # Keep OCR available until backend requirements are installed.
    SpellChecker = None


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_ROOT / "custom_dataset"
LABELS_PATH = DATASET_DIR / "labels.csv"
CUSTOM_WORDS_PATH = DATASET_DIR / "custom_words.txt"
WORD_PATTERN = re.compile(r"[^\W\d_]+(?:['’][^\W\d_]+)*", re.UNICODE)
VALID_CUSTOM_WORD = re.compile(r"[^\W\d_]+(?:['’][^\W\d_]+)*\Z", re.UNICODE)

_spell = SpellChecker(language="en", distance=1) if SpellChecker else None
_loaded_domain_words = set()


def _load_domain_words():
    words = set()
    if LABELS_PATH.exists():
        try:
            with LABELS_PATH.open("r", encoding="utf-8-sig", newline="") as labels_file:
                for row in csv.DictReader(labels_file):
                    for match in WORD_PATTERN.finditer(row.get("text", "")):
                        words.add(match.group(0).casefold())
        except (OSError, csv.Error):
            pass

    if CUSTOM_WORDS_PATH.exists():
        try:
            for line in CUSTOM_WORDS_PATH.read_text(encoding="utf-8").splitlines():
                word = line.strip().casefold()
                if VALID_CUSTOM_WORD.fullmatch(word):
                    words.add(word)
        except OSError:
            pass
    return words


def _refresh_domain_words():
    if _spell is None:
        return
    new_words = _load_domain_words() - _loaded_domain_words
    if new_words:
        _spell.word_frequency.load_words(new_words)
        _loaded_domain_words.update(new_words)


def _match_case(source, replacement):
    if source.isupper():
        return replacement.upper()
    if source[:1].isupper():
        return replacement.capitalize()
    return replacement


def suggest_corrections(text):
    """Return (suggested text, per-word suggestions); never mutates input."""
    if not text or _spell is None:
        return text or "", []

    _refresh_domain_words()
    corrections = []

    def replace_word(match):
        original = match.group(0)
        normalized = original.casefold()
        # Short words, acronyms, and numeric-like tokens are easy to overcorrect.
        if len(normalized) < 3 or original.isupper() or normalized not in _spell.unknown([normalized]):
            return original

        candidate = _spell.correction(normalized)
        if not candidate or candidate == normalized:
            return original

        replacement = _match_case(original, candidate)
        corrections.append({"original": original, "suggestion": replacement})
        return replacement

    suggested = WORD_PATTERN.sub(replace_word, text)
    return suggested, corrections


def add_custom_word(word):
    """Persist a user-approved word so future OCR won't flag it."""
    normalized = (word or "").strip().casefold()
    if not normalized or len(normalized) > 64 or not VALID_CUSTOM_WORD.fullmatch(normalized):
        raise ValueError("Enter a single word containing letters or apostrophes.")
    if _spell is None:
        raise RuntimeError("Spell checking is unavailable; install backend requirements first.")

    DATASET_DIR.mkdir(parents=True, exist_ok=True)
    existing = set()
    if CUSTOM_WORDS_PATH.exists():
        existing = {line.strip().casefold() for line in CUSTOM_WORDS_PATH.read_text(encoding="utf-8").splitlines()}
    if normalized not in existing:
        with CUSTOM_WORDS_PATH.open("a", encoding="utf-8", newline="\n") as custom_file:
            custom_file.write(normalized + "\n")
    _spell.word_frequency.load_words([normalized])
    _loaded_domain_words.add(normalized)
    return normalized


def is_spellchecker_available():
    return _spell is not None
