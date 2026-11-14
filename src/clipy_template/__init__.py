from typing import Any
from unittest.mock import patch

import typer
from rich.box import SQUARE
from rich.panel import Panel as _Panel
from typer_config.decorators import use_toml_config

from .commands import COMMAND_APPS


# 创建新边框样式的 Panel
class Panel(_Panel):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, box=SQUARE, **kwargs)


app = typer.Typer(no_args_is_help=True)


# 加载全局 TOML 配置，空函数，具体功能由装饰器提供
@app.callback()
@use_toml_config()
def _load_config() -> None:
    pass


# 统一注册子 Typer 应用
for app_name, sub_app in COMMAND_APPS.items():
    app.add_typer(sub_app, name=app_name)


def main() -> None:
    # 注入修改的 Panel
    with patch("typer.rich_utils.Panel", Panel):
        app()
