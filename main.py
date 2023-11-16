"""
Project entry point
"""
import sys
from aiolchemy.management import CommandManager, commands


def main():
    sys.dont_write_bytecode = True
    # create manager to select command to execute
    manager = CommandManager(sys.argv)
    # pass command classes to manager
    manager.add_commands(commands)
    # execute selected by manager command
    manager.execute()


if __name__ == "__main__":
    main()  