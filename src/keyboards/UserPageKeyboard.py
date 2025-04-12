from typing import Optional

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class PageCallbackFactory(CallbackData, prefix="user_page"):
    action: str
    value: Optional[int]


def get_keyboard_fab():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="<-", callback_data=PageCallbackFactory(action="change", value=-50)
    )
    builder.button(
        text="->", callback_data=PageCallbackFactory(action="change", value=50)
    )
    return builder.as_markup()
