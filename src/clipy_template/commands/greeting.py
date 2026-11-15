from typing import Annotated

import typer
from rich.console import Console

# 子 Typer
app = typer.Typer(help="示例命令", no_args_is_help=True)

console = Console()


@app.command()
def hello(name: Annotated[str, typer.Argument(help="user's name")] = "") -> None:
    """示例子命令"""
    if name:
        console.print(f"Hello, [bold cyan]{name}[/bold cyan]")
        return
    console.print("Hello from cli-template!")
