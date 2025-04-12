import yaml
from pydantic import BaseModel, SecretStr


def open_config(config_file):
    with open(config_file, encoding="utf-8") as file:
        return yaml.safe_load(file)


class User(BaseModel):
    level: str | int


class TelegramModel(BaseModel):
    token: SecretStr
    access: dict[str | int, User]


class DBModel(BaseModel):
    path: str


class ConfigModel(BaseModel):
    telegram: TelegramModel
    database: DBModel
