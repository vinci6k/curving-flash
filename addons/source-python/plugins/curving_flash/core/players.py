# ../curving_flash/core/players.py

# Source.Python
from messages import HintText
from players.entity import Player

# Curving Flash
from .constants import ThrowingMode
from .strings import strings


__all__ = (
    'PlayerCF',
)


switch_message = {
    True: HintText(strings['curving_mode'].tokenized(help=strings['help'])),
    False: HintText(strings['normal_mode'])
}


class PlayerCF(Player):
    """Custom Player class.

    Args:
        index (int): A valid player index.
        caching (bool): Check for a cached instance?

    Attributes:
        last_inspect_time (float): Last time (seconds since the epoch) the
            player inspected their weapon.
        should_curve_flash (bool): Should the player curve flashbangs when
            throwing them?
        throwing_mode (ThrowingMode): How should the player throw flashbangs?
    """

    def __init__(self, index, caching=True):
        """Initializes the object."""
        super().__init__(index, caching)

        self.last_inspect_time = 0.0
        self.should_curve_flash = False
        self.throwing_mode = ThrowingMode.NORMAL

    def switch_flash_mode(self):
        """Inverts the player's flashbang throwing mode."""
        self.should_curve_flash = not self.should_curve_flash
        switch_message[self.should_curve_flash].send(self.index)

        self.emit_sound(
            sample='weapons/auto_semiauto_switch.wav',
            attenuation=2.4,
            volume=0.3
        )

    def on_death(self):
        """Called when the player dies."""
        self.should_curve_flash = False
        self.throwing_mode = ThrowingMode.NORMAL
