from src.yamlparser import ConfigModel, open_config

def get_config() -> ConfigModel:
    return ConfigModel(**open_config("config.yaml"))
