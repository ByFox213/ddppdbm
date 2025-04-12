import logging
import sys

from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.yamlparser import ConfigModel
from bot import Bot

dp = Dispatcher()


async def start_bot(config: ConfigModel):
    bot = Bot(
        config=config,
        dp=dp,
        token=config.telegram.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await bot.setup_handlers()
    await dp.start_polling(bot)
