# ../curving_flash/core/players.py

# Source.Python
from engines.sound import Sound
from messages import HintText
from players.dictionary import PlayerDictionary
from players.entity import Player


switch_message = {
    True: HintText(' ' * 22 + ('Switched to curving mode\n'
        '(left click to curve left, right click to curve right)')),
    False: HintText('Switched to normal')
}


class PlayerCF(Player):
    """Custom Player class.
    
    Args:
        index (int): A valid player index.
        caching (bool): Check for a cached instance?

    Attributes:
        should_curve_flash (bool): Should the player curve flashbangs when
            throwing them?
        switch_sound (Sound): Sound that's played when the player switches
            their flashbang throwing mode.
    """

    def __init__(self, index, caching=True):
        """Initializes the object."""
        super().__init__(index, caching)
        self.should_curve_flash = False
        self.switch_sound = Sound(
            sample='weapons/auto_semiauto_switch.wav',
            # Emit the sound from the player.
            index=self.index,
            volume=0.3,
            # How quickly does the sound fade based on distance?
            attenuation=2.4)

    def switch_flash_mode(self):
        """Inverts the player's flashbang throwing mode."""
        self.should_curve_flash = not self.should_curve_flash
        self.switch_sound.play()
        switch_message[self.should_curve_flash].send(self.index)

    def on_death(self):
        """Called when the player dies."""
        self.should_curve_flash = False


player_instances = PlayerDictionary(PlayerCF)



