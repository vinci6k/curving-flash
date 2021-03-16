# ../curving_flash/core/memory.py

# Source.Python
from memory.manager import manager

# Curving Flash
from .paths import CF_PLUGIN_DATA_PATH


__all__ = (
    'CBaseGrenade',
)


CBaseGrenade = manager.create_type_from_file(
    'CBaseGrenade', CF_PLUGIN_DATA_PATH / 'CBaseGrenade.ini'
)
