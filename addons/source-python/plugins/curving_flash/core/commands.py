# ../curving_flash/core/commands.py

# Python
from time import time

# Source.Python
from commands.client import ClientCommand

# Curving Flash
from .constants import COMMAND_INTERVAL
from .players import PlayerCF


@ClientCommand('+lookatweapon')
def inspect_weapon(command, index):
    """Called when a player inspects their weapon."""
    # Get the PlayerCF instance.
    player = PlayerCF(index)
    inspect_time = time()

    # Has the player recently used the command? (anti-spam measure)
    if inspect_time - player.last_inspect_time < COMMAND_INTERVAL:
        return

    player.last_inspect_time = inspect_time

    try:
        # Let's see which weapon the player is inspecting.
        weapon_name = player.active_weapon.classname
    except AttributeError:
        # The player doesn't have any weapons, don't go further.
        return

    # Is the player holding a flashbang?
    if weapon_name == 'weapon_flashbang':
        player.switch_flash_mode()
