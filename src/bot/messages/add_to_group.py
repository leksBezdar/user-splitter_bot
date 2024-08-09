from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.messages.base import BaseMessageBuilder


class AddToGroupMessageBuilder(BaseMessageBuilder):
    _text = "🤝 Хорошо, давай выберем группу, в которую ты попадешь!"
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1️⃣ Выбрать вручную",
                    callback_data="add_group_manually",
                )
            ],
            [
                InlineKeyboardButton(
                    text="2️⃣ Выбрать случайную", callback_data="add_group_randomly"
                )
            ],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="start")],
        ],
    )


class AddGroupManuallyMessageBuilder(BaseMessageBuilder):
    _text = "👥 Ты нажал выбрать группу вручную. Пожалуйста, нажми на ту, которая тебя заинтересовала."
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="group")],
        ],
    )


class AddGroupRandomlyMessageBuilder(BaseMessageBuilder):
    _text = "👥 Ты нажал выбрать случайную группу. Ниже будет представлена ссылка для перехода в нее, удачи!"
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="group")],
        ],
    )


class GetGroupRequestMessageBuilder(BaseMessageBuilder):
    def __init__(self, group_oid: str) -> None:
        self.group_oid = group_oid

    @property
    def text(self) -> str:
        return ""
