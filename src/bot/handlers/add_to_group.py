import logging

from aiogram import types

from src.bot.messages.add_to_group import (
    AddGroupRandomlyMessageBuilder,
    AddToGroupMessageBuilder,
    AddGroupManuallyMessageBuilder,
)
from src.bot.utils import callback_handler_wrapper

logger = logging.getLogger(__name__)


@callback_handler_wrapper
async def start_add_group_handler(message: types.Message) -> None:
    content = AddToGroupMessageBuilder().build()
    await message.reply(**content)


@callback_handler_wrapper
async def add_group_manually_handler(message: types.Message) -> None:
    content = AddGroupManuallyMessageBuilder().build()
    await message.reply(**content)


@callback_handler_wrapper
async def add_group_randomly_handler(message: types.Message) -> None:
    content = AddGroupRandomlyMessageBuilder().build()
    await message.reply(**content)
