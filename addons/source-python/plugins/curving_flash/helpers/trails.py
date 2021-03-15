# ../curving_flash/helpers/trails.py

# Source.Python
from colors import Color
from effects.base import TempEntity
from engines.precache import Model
from listeners import OnServerActivate


__all__ = (
    'create_trails',
)


default_model = Model('materials/sprites/laserbeam.vmt')


@OnServerActivate
def on_server_activate(edicts, edict_count, max_clients):
    """Called when the new map gets fully loaded."""
    initialize_trails()


trails = []


def initialize_trails():
    """Creates and stores two TempEntity instances used for grenade trails."""
    # Make sure to remove any references to old TempEntity instances.
    trails.clear()
    # Add two new instances to the list.
    trails.extend([
        TempEntity(
            temp_entity='BeamFollow', 
            model=default_model, 
            start_width=0.4, 
            end_width=0.4, 
            color=Color(255, 255, 255), 
            alpha=100, 
            life_time=0.4, 
            fade_time=0.4),
        TempEntity(
            temp_entity='BeamFollow', 
            model=default_model, 
            start_width=0.1, 
            end_width=0.1, 
            color=Color(255, 255, 255), 
            alpha=50, 
            life_time=0.6, 
            fade_time=0.2)
    ])


def create_trails(entity_index):
    for trail in trails:
        trail.entity_index = entity_index
        trail.create()


initialize_trails()

