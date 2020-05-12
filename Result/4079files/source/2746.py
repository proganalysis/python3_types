from commands import CommandReturn
from commands.client import ClientCommandFilter
from engines.server import engine_server
from messages import SayText2
from players.entity import Player

from .filters import Filter
from .manager import command_manager
from ..permissions import check_permission


@ClientCommandFilter
def on_client_command(array, index):
    command = array[0]

    if command in command_manager:
        try:
            method, length, permission = command_manager[command]
        except:
            method, length = command_manager[command]

        player = Player(index)

        if method and check_permission(player, permission):
            args = [player]
            for i in range(1, len(array)):
                args.append(array[i])

            if len(args) == length:
                method(*args)
            else:
                engine_server.client_printf(
                    player.edict,
                    'CA - This command requires {} arguments.\n'.format(length)
                )

            return CommandReturn.BLOCK

    return CommandReturn.CONTINUE
