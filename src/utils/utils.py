import logging

from aiogram.types import Message


__all__ = ("clamp", "log")


def clamp(mininum, x, maximum):
    return max(mininum, min(x, maximum))


def log(msg: Message):
    logging.info(
        msg=f"id: {msg.from_user.id}, first_name: {msg.from_user.first_name} | {msg.text}"  # noqa: E501
    )
