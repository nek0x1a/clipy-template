from typer_config import conf_callback_factory
from typer_config.decorators import use_config
from typer_config.loaders import loader_transformer, toml_loader


def command_config(command_name: str):
    loader = loader_transformer(
        toml_loader,
        config_transformer=lambda config: config.get(command_name, {}),
    )
    callback = conf_callback_factory(loader)
    return use_config(callback)
