# clipy-template

一个使用 Typer 构建的 python cli 样板，以便快速开发。

## 使用

1. 克隆本项目并使用新项目名: `git clone --depth 1 https://github.com/nek0x1a/clipy-template.git <new_project>`。
2. 修改 `pyproject.toml` 内容和 `./src/clipy-template` 适配新项目名。
3. 在 `./src/<new_project>/commands/` 中新建子命令逻辑入口函数。
4. 将新子命令引入 `./src/<new_project>/commands/__init__.py` 中的 `COMMAND_FUNCTIONS` 即可自动注册。
