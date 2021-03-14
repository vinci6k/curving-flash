# ../curving_flash/curving_flash.py

# Source.Python
from events import Event
from entities.entity import BaseEntity
from entities.helpers import index_from_inthandle
from mathlib import Vector, QAngle

# Curving Flash
from .core.commands import inspect_weapon
from .core.flashbangs import CurvingFlash
from .core.listeners import OnFlashbangCreated
from .core.players import player_instances


@OnFlashbangCreated
def on_flashbang_created(index, owner_handle):
    """Called when a 'flashbang_projectile' has been fully created."""
    player = player_instances.from_inthandle(owner_handle)

    # Does the player want to curve the flashbang?
    if not player.should_curve_flash:
        return

    right = Vector()
    # Get the 'right' direction based on the player's view.
    QAngle.get_angle_vectors(player.view_angle, None, right, None)

    # Get the player's viewmodel.
    viewmodel = BaseEntity(
        index_from_inthandle(player.get_property_int('m_hViewModel')))
    # Get the current viewmodel animation sequence.
    sequence = viewmodel.get_network_property_uchar('m_nSequence')

    # Did the player throw the flashbang with left click?
    # (2 = left click, 4 = right click / both clicks at the same time)
    if sequence == 2:
        # Invert the direction.
        right *= -1.0

    flashbang = CurvingFlash(index)
    flashbang.curve(
        start_direction=player.view_vector, 
        curve_direction=right, 
        curve_delay=0.1
        )


@Event('player_death')
def player_death(event):
    player_instances.from_userid(event['userid']).on_death()
