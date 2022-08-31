# Curving Flash
This plugin adds the ability to throw flashbangs in a curve to your server.

<img src="https://media2.giphy.com/media/eJYGpsGLCFhlb5lZEZ/giphy.gif" width="412px"/> <img src="https://media0.giphy.com/media/lMrUsQthIPsfoJmXhY/giphy.gif" width="412px"/>

See the plugin in action: https://youtu.be/GoANDNFMt2A

## Installation
1. [Install Source.Python](http://wiki.sourcepython.com/general/installation.html).
2. Download [the latest release](https://github.com/vinci6k/curving-flash/releases) of Curving Flash.
3. Extract the files into your game server's root folder (../csgo/).
4. Add `sp plugin load curving_flash` to your autoexec file (../csgo/cfg/autoexec.cfg).
5. Restart your server.

## Usage
While holding a flashbang, press your weapon inspect key (F by default) to change the throwing mode.

## Integration with other plugins
Do you want to use Curving Flash as part of another plugin? Maybe as a passive skill or an item that can be picked up?

If the answer is yes, head over to `../csgo/cfg/source-python/curving_flash/config.cfg` and set `cf_package_mode` to **1**. This will disable the default plugin behavior, and as such, players will no longer be able to change their throwing mode on their own.

Now the power to change the throwing mode of players lies within your plugin. There are two ways to change a player's throwing mode.

1. Use the PlayerCF class.
    ```py
    from curving_flash.core.constants import ThrowingMode
    from curving_flash.core.players import PlayerCF

    # Disables curving for this player, they can only throw flashbangs normally.
    # All players will have this mode set by default.
    PlayerCF(index).throwing_mode = ThrowingMode.NORMAL

    # Default plugin behavior - player can inspect their flashbang to change their
    # throwing mode.
    PlayerCF(index).throwing_mode = ThrowingMode.DEFAULT

    # All flashbangs thrown by this player will curve.
    PlayerCF(index).throwing_mode = ThrowingMode.ALWAYS_CURVE
    ```
2. Use the `cf_set_mode <userid> <mode>` server command, where `mode` can be:  
   * **0**: Normal (default flashbang throw)  
   * **1**: Player controlled (default plugin behavior)  
   * **2**: Always curve

**NOTE:** Keep in mind that the throwing mode resets whenever the player dies.

## Supported Games
Counter-Strike: Global Offensive
