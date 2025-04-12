import enum

from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.config import get_config


class PermissionLevel(enum.IntEnum):
    admin = 10
    moderator = 2
    user = 1
    denied = 0


class AuthFilter(BaseFilter):
    def __init__(self, minimum_level=PermissionLevel.user):
        self.level = minimum_level
        self.tc = get_config().telegram.access

    async def get_permission_level(self, user_id):
        user = self.tc.get(user_id)
        if user:
            return PermissionLevel[user.level]

        return PermissionLevel.denied

    async def __call__(self, message: Message) -> bool:
        user_perms = await self.get_permission_level(message.from_user.id)
        return user_perms >= self.level
