import click

from .commands import add_command, delete_command, list_command, sync_command, update_command


def create_workspace_cli_group():
    """
    Commands for managing a dagster cloud workspace.
    """

    group = click.Group(name="workspace")
    group.add_command(add_command)
    group.add_command(update_command)
    group.add_command(delete_command)
    group.add_command(list_command)
    group.add_command(sync_command)
    return group


workspace_cli = create_workspace_cli_group()
