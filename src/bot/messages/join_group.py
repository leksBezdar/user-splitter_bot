from typing import Any
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from gateways.postgresql.repositories.base import IGroupRepository
from src.bot.messages.base import BaseMessageBuilder


class JoinToGroupMessageBuilder(BaseMessageBuilder):
    _text = "🤝 Хорошо, давай выберем группу, в которую ты попадешь!"
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1️⃣ Выбрать вручную",
                    callback_data="join_group_manually",
                )
            ],
            [
                InlineKeyboardButton(
                    text="2️⃣ Выбрать случайную", callback_data="join_group_randomly"
                )
            ],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="start")],
        ],
    )


class JoinGroupManuallyMessageBuilder(BaseMessageBuilder):
    _text = "👥 Ты нажал выбрать группу вручную. Пожалуйста, нажми на ту, которая тебя заинтересовала."
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="group")],
        ],
    )

    def __init__(self, group_repository: IGroupRepository) -> None:
        self.group_repository = group_repository

    async def update_reply_markup(self) -> None:
        groups = await self.group_repository.get_all()
        keyboard = [
            [InlineKeyboardButton(text=group.name, callback_data=f"group_{group.oid}")]
            for group in groups
        ]
        keyboard.append([InlineKeyboardButton(text="🔙 Назад", callback_data="group")])
        self._reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    @property
    def reply_markup(self) -> Any | None:
        if self._reply_markup is None:
            raise ValueError(
                "reply_markup has not been initialized. Call update_reply_markup first."
            )
        return self._reply_markup

    async def build(self) -> dict:
        await self.update_reply_markup()
        return {"text": self._text, "reply_markup": self.reply_markup}


class JoinGroupRandomlyMessageBuilder(BaseMessageBuilder):
    _text = "👥 Ты нажал выбрать случайную группу. Ниже будет представлена ссылка для перехода в нее, удачи!"
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="group")],
        ],
    )


class GetGroupRequestMessageBuilder(BaseMessageBuilder):
    def __init__(self, oid: str) -> None:
        self.oid = oid

    @property
    def text(self) -> str:
        return ""
