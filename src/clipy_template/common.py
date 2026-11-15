import logging

from rich.console import Console
from rich.logging import RichHandler

console = Console()


def _setup_logger() -> logging.Logger:

    logger = logging.getLogger("clipy-template")
    logger.setLevel(logging.DEBUG)
    log_handle = RichHandler(
        console=console,
        rich_tracebacks=True,
        markup=True,
        omit_repeated_times=False,
        log_time_format="[%Y-%m-%d %X]",
    )
    log_handle.setFormatter(logging.Formatter("%(message)s"))

    logger.addHandler(log_handle)
    logger.propagate = False
    return logger


logger = _setup_logger()
