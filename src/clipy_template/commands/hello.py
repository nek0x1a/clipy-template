from typing import Annotated

import typer
from rich.console import Console

console = Console()


def hello(name: Annotated[str, typer.Argument(help="user's name")] = "") -> None:
    if name:
        console.print(f"Hello, [bold cyan]{name}[/bold cyan]")
        return
    print("Hello from cli-template!")
