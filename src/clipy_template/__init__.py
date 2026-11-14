import typer

from .commands import COMMAND_FUNCTIONS

app = typer.Typer()
command_register = app.command()
for cmd in COMMAND_FUNCTIONS:
    command_register(cmd)


def main() -> None:
    app()
