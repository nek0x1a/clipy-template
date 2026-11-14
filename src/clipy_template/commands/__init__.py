from .greeting import app as greeting_app

# 需要自动注册的子 Typer
COMMAND_APPS = {"greeting": greeting_app}
