# ../curving_flash/core/commands.py

# Python
import time

# Source.Python
from commands.client import ClientCommand
from weapons.dictionary import WeaponDictionary

# Curving Flash
from .players import player_instances
from .constants import COMMAND_INTERVAL


_last_command_time = {}
weapon_instances = WeaponDictionary()


@ClientCommand('+lookatweapon')
def inspect_weapon(command, index):
    # Has the player recently used the command? (anti-spam measure)
    if index in _last_command_time:
        if time.time() - _last_command_time[index] < COMMAND_INTERVAL:
            return

    _last_command_time[index] = time.time()

    # Get the Player instance.
    player = player_instances[index]
    try:
        # Get the Weapon instance the player is currently holding.
        weapon = weapon_instances.from_inthandle(player.active_weapon_handle)
    except OverflowError:
        # Invalid inthandle.
        return

    # Don't go further if the player isn't holding a flashbang.
    if 'weapon_flashbang' not in weapon.classname:
        return

    player.switch_flash_mode()
