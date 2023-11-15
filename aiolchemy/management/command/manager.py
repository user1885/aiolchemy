from .base import NullCommand
from .commands import *

# commands to pass later
commands = (
    BrewCommand,
    MakeRecipeCommand,
)


class CommandManager:
    """
    Manage selected commands by args and execute
    """
    def __init__(self, args) -> None:
        self.args = args
        self.commands = []
        
    def add_command(self, command: BaseCommand):
        self.commands.append(command)

    def add_commands(self, commands):
        self.commands.extend(commands)

    def execute(self):
        command = self._find_command()
        command(self.args).execute()

    def _find_command(self):
        # filter commands by first element
        command_arg = self.args[1] if len(self.args) > 1 else None
        if command_arg is None:
            return NullCommand
        for command in self.commands:
            if command.name == command_arg:
                return command