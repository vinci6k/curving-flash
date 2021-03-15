# ../curving_flash/curving_flash.py

# Source.Python
from entities.entity import Entity
from events import Event
from mathlib import Vector

# Curving Flash
from .core.commands import inspect_weapon
from .core.flashbangs import CurvingFlash
from .core.listeners import OnFlashbangCreated
from .core.players import PlayerCF


@OnFlashbangCreated
def on_flashbang_created(index, owner_handle):
    """Called when a 'flashbang_projectile' has been fully created."""
    player = PlayerCF.from_inthandle(owner_handle)

    # Does the player want to curve the flashbang?
    if not player.should_curve_flash:
        return

    right = Vector()
    # Get the 'right' direction based on the player's view.
    player.view_angle.get_angle_vectors(right=right)

    # Get the player's view model.
    view_model = Entity.from_inthandle(player.get_property_int('m_hViewModel'))
    # Get the current view model animation sequence.
    sequence = view_model.get_network_property_uchar('m_nSequence')

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
    """Called when a player dies."""
    PlayerCF.from_userid(event['userid']).on_death()
