import asyncio
import logging

from aiogram import Dispatcher, Bot

from config import BOT_TOKEN_POLLING
from router import main_router

logger = logging.getLogger(__name__)


async def run_polling():
    bot = Bot(token=BOT_TOKEN_POLLING)
    dp = Dispatcher()

    dp.include_router(main_router)

    await dp.start_polling(
        bot,
        allowed_updates=[
            "channel_post",
        ],
    )


def main():
    logger.info("Start polling bot")
    asyncio.run(run_polling())
