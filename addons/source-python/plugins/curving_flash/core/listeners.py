# ../curving_flash/core/listeners.py

# Source.Python
from listeners import ListenerManager, ListenerManagerDecorator
from listeners import OnEntityCreated
from listeners.tick import Delay


__all__ = (
    'OnFlashbangCreated',
    )


class OnFlashbangCreated(ListenerManagerDecorator):
    """Register/unregister a OnFlashbangCreated listener."""
    manager = ListenerManager()


@OnEntityCreated
def on_entity_created(base_entity):
    try:
        index = base_entity.index
    except ValueError:
        return

    if 'flashbang_projectile' in base_entity.classname:
        # Get the owner of the flashbang.
        owner_handle = base_entity.owner_handle
        # No owner? (invalid inthandle)
        if owner_handle == -1:
            return

        # Delay the call by a single frame, otherwise the flashbang won't be
        # properly initialized.
        Delay(0, OnFlashbangCreated.manager.notify, (index, owner_handle))
