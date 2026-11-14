import typer

from .commands import COMMAND_FUNCTIONS, command_config

app = typer.Typer()
for cmd in COMMAND_FUNCTIONS:
    configured_cmd = command_config(cmd.__name__)(cmd)
    app.command()(configured_cmd)


def main() -> None:
    app()
