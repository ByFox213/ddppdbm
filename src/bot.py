import logging

from aiogram import Dispatcher, Bot as BaseBot

from src.yamlparser import ConfigModel

import handlers.admin as admin_router
import handlers.user as user_router

_log = logging.getLogger(__name__)


class Bot(BaseBot):
    def __init__(self, config: ConfigModel, dp: Dispatcher, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config = config
        self.dp = dp

    async def setup_handlers(self):
        self.dp.include_router(admin_router.prepare_router())
        self.dp.include_routers(
            admin_router.prepare_router(), user_router.prepare_router()
        )
