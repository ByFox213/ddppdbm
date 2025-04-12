import asyncio
import telegram
from src.yamlparser import ConfigModel, open_config


async def main() -> None:
    await telegram.start_bot(ConfigModel(**open_config("config.yaml")))


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
