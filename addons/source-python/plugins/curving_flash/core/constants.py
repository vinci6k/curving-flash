# ../curving_flash/core/constants.py

# Source.Python
from mathlib import Vector


__all__ = (
    'UP',
    'COMMAND_INTERVAL'
)


# Directional vector.
UP = Vector(0, 0, 0.1)

# How often the '+lookatweapon' client command can be triggered. (in seconds)
COMMAND_INTERVAL = 0.25
