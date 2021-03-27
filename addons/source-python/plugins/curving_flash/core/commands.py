# ../curving_flash/core/commands.py

# Python
from time import time

# Source.Python
from core import echo_console
from commands.client import ClientCommand
from commands.typed import TypedServerCommand

# Curving Flash
from .constants import COMMAND_INTERVAL, ThrowingMode
from .config import package_mode
from .players import PlayerCF


@ClientCommand('+lookatweapon')
def inspect_weapon(command, index):
    """Called when a player inspects their weapon."""
    # Get the PlayerCF instance.
    player = PlayerCF(index)

    # Is the plugin running in utility/custom package mode?
    if package_mode.get_int() and player.throwing_mode != ThrowingMode.DEFAULT:
        return

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


@TypedServerCommand('cf_set_mode')
def set_throwing_mode(command_info, userid:int, mode_int:int):
    """Server command used for setting the grenade throwing mode for a player.

    Args:
        userid (int): Userid of the player.
        mode_int (int): Throwing mode.

    Examples:
        >>> cf_set_mode 5 1
        Player with userid 5 can change their throwing mode by inspecting their
        weapon (F by default).

        >>> cf_set_mode 5 0
        Player with userid 5 will throw flashbangs normally.

        >>> cf_set_mode 3 2
        Player with userid 3 will always throw curving flashbangs.
    """
    command_str = command_info.command[0]

    try:
        # Is this a valid throwing mode?
        mode = ThrowingMode(mode_int)
    except ValueError:
        echo_console(f'{command_str}: invalid mode -> {mode_int}')
        return

    try:
        # Try to get a PlayerCF instance.
        player = PlayerCF.from_userid(userid)
    except ValueError:
        echo_console(f'{command_str}: invalid userid -> {userid}')
        return

    # Are we going back to default game behavior?
    if mode == ThrowingMode.NORMAL:
        player.should_curve_flash = False

    # Or should all flashbangs curve?
    elif mode == ThrowingMode.ALWAYS_CURVE:
        player.should_curve_flash = True

    player.throwing_mode = mode
