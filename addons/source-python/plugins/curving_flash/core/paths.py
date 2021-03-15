# ../curving_flash/core/paths.py

# Source.Python
from paths import TRANSLATION_PATH

# Curving Flash
from ..info import info


__all__ = (
    'CF_TRANSLATION_PATH',
)


CF_TRANSLATION_PATH = TRANSLATION_PATH / info.name
