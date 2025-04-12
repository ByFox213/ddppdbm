from aiogram import Router
from aiogram.filters import Command
from aiogram import F

from src.middlewares.DatabaseMiddleware import DatabaseMiddleware

from .admin import *
from src.keyboards.UserPageKeyboard import PageCallbackFactory
from src.filters.AuthFilter import AuthFilter, PermissionLevel


def prepare_router() -> Router:
    admin_router = Router(name="admin")

    admin_router.message.filter(AuthFilter(minimum_level=PermissionLevel.moderator))
    admin_router.message.middleware(DatabaseMiddleware())

    admin_router.message.register(help_message, Command("help"))
    admin_router.message.register(chat, Command("chat"))
    admin_router.message.register(
        get_user,
        Command("get_user"),
    )
    admin_router.message.register(
        get_user_by_id, F.text.regexp(r"^\/user(\d+)$").as_("digits")
    )
    admin_router.message.register(freeze, Command("freeze"))
    ###
    admin_router.message.register(
        set_user,
        Command("set_user"),
        AuthFilter(minimum_level=PermissionLevel.admin),
    )
    admin_router.message.register(
        prem, Command("prem"), AuthFilter(minimum_level=PermissionLevel.admin)
    )

    admin_router.callback_query.middleware(DatabaseMiddleware())
    admin_router.callback_query.register(
        scroll_user_list_keyboard, PageCallbackFactory.filter()
    )
    return admin_router
