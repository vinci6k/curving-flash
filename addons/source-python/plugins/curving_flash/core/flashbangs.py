# ../curving_flash/core/flashbangs.py

# Source.Python
from entities.constants import MoveType
from entities.entity import Entity

# Curving Flash
from .constants import UP
from ..helpers.trails import create_trails


class CurvingFlash(Entity):
    """Flashbang that curves when thrown.

    Args:
        index (int): A valid entity index.
        caching (bool): Check for a cached instance?

    Attributes:
        curve_velocity (Vector): Turning speed of the flashbang.
        reverse_velocity (Vector): Reverse speed of the flashbang. Used to make
            the flashbang slow down from the initial velocity and begin going
            into the opposite direction.
        think (Repeat): Instance of Repeat() used for looping the `_think()`
            function.
    """

    def __init__(self, index, caching=False):
        """Initializes the object."""
        super().__init__(index, caching)
        
        self.curve_velocity = None
        self.reverse_velocity = None
        self.think = self.repeat(self._think)
        # Add some visual effects to the flashbang.
        create_trails(entity_index=index)

    def curve(self, start_direction, curve_direction, curve_delay):
        """Begins curving the 'flashbang_projectile' in the given direction.
        
        Note:
            The specified vectors must be normalized!

        Args:
            start_direction (Vector): Direction of the projectile immediately
                after spawning.
            curve_direction (Vector): Direction towards which the projectile
                will curve / turn.
            curve_delay (float): After how long should the projectile begin
                to curve? (in seconds)
        """
        # Disable the gravity.
        self.move_type = MoveType.FLY
        # Curve the 'flashbang_projectile' in the opposite direction a bit.
        start_velocity = (start_direction + (curve_direction * -0.28)) * 400
        self.teleport(None, self.angles, start_velocity)
        # Get 22% of the initial velocity and invert it.
        self.reverse_velocity = start_velocity * -0.22
        self.curve_velocity = (curve_direction + UP) * 120

        # Start curving the 'flashbang_projectile' in the proper direction.
        self.delay(curve_delay, self.think.start, (0.1,))
        self.delay(curve_delay + 0.55, self.detonate)

    def _think(self):
        # Did the 'flashbang_projectile' touch something while curving?
        if self.get_network_property_int('m_nBounces') > 0:
            self.think.stop()
            return

        # Curve the 'flashbang_projectile' to the side and pull it a bit 
        # towards the starting position.
        self.set_datamap_property_vector('m_vecBaseVelocity', 
            self.curve_velocity + self.reverse_velocity)
