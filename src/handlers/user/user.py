from aiogram.types import Message

from src.utils import log


async def start(message: Message) -> None:
    log(message)
    await message.reply("This bot rules S-DDRace / DDPP SQLite3 Database.")
