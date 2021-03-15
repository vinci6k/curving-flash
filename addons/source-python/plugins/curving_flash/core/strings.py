# ../curving_flash/core/strings.py

# Source.Python
from translations.strings import LangStrings

# Curving Flash
from .paths import CF_TRANSLATION_PATH


__all__ = (
    'strings',
)


strings = LangStrings(CF_TRANSLATION_PATH / 'strings')
