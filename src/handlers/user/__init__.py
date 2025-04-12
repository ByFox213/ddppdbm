from aiogram import Router
from aiogram.filters import CommandStart

from .user import *


def prepare_router() -> Router:
    user_router = Router(name="user")

    user_router.message.register(user.start, CommandStart())

    return user_router
