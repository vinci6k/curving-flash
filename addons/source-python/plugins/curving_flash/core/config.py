# ../curving_flash/core/config.py

# Source.Python
from config.manager import ConfigManager

# Curving Flash
from ..info import info


__all__ = (
    'package_mode',
    )


# Create a config file in the '../cfg/source-python/curving_flash' folder.
with ConfigManager(f'{info.name}/config.cfg', 'cf_') as config:
    config.header = f'{info.verbose_name} Settings'

    package_mode = config.cvar(
        'package_mode', 0,
        'Should the plugin act as a utility/custom package for other plugins?'
        )
