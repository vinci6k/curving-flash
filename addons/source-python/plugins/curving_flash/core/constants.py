# ../curving_flash/core/constants.py

# Python
from enum import IntEnum

# Source.Python
from mathlib import Vector


__all__ = (
    'UP',
    'COMMAND_INTERVAL',
    'ThrowingMode',
)


# Directional vector.
UP = Vector(0, 0, 0.1)

# How often the '+lookatweapon' client command can be triggered. (in seconds)
COMMAND_INTERVAL = 0.25


class ThrowingMode(IntEnum):
    """Determines the throwing capabilities of a player."""
    # Normal flashbang throw.
    NORMAL = 0
    # Default plugin behavior - player has to use their weapon inspect key
    # (F by default) in order to change their throwing mode.
    DEFAULT = 1
    # All flashbangs thrown by this player will curve.
    ALWAYS_CURVE = 2
