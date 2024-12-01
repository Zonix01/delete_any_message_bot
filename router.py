from aiogram import Bot, Router, F
from aiogram.types import Message

main_router = Router()


@main_router.channel_post()
async def catch_any_message(message: Message, bot: Bot):
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id
    )
