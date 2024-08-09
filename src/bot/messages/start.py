from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.messages.base import BaseMessageBuilder


class StartMessageBuilder(BaseMessageBuilder):
    _text = "👋 Привет! Я твой лучший бот-помощник. Чем могу помочь?"

    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Выбрать группу", callback_data="group"),
                InlineKeyboardButton(text="Помощь", url="https://aiogram.dev/"),
            ]
        ],
    )
