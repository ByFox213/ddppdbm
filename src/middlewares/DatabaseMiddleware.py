from typing import Dict, Any

import aiosqlite
from aiogram import BaseMiddleware
from aiogram.types import Message

from src.config import get_config

class DatabaseMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass
    async def __call__(self, handler, event: Message, data: Dict[str, Any]):
        db_path = get_config()['database']['path']
        async with aiosqlite.connect(db_path) as db:
            data['db'] = db
            print("database loaded")
            return await handler(event, data)

