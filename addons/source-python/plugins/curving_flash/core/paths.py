# ../curving_flash/core/paths.py

# Source.Python
from paths import PLUGIN_DATA_PATH, TRANSLATION_PATH

# Curving Flash
from ..info import info


__all__ = (
    'CF_PLUGIN_DATA_PATH',
    'CF_TRANSLATION_PATH'
)


CF_PLUGIN_DATA_PATH = PLUGIN_DATA_PATH / info.name
CF_TRANSLATION_PATH = TRANSLATION_PATH / info.name
