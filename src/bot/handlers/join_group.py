import logging

from aiogram import types

from core.containers import get_container
from gateways.postgresql.repositories.base import IGroupRepository
from bot.messages.join_group import (
    JoinGroupRandomlyMessageBuilder,
    JoinToGroupMessageBuilder,
    JoinGroupManuallyMessageBuilder,
)
from src.bot.utils import callback_handler_wrapper

logger = logging.getLogger(__name__)


@callback_handler_wrapper
async def start_join_group_handler(message: types.Message) -> None:
    content = JoinToGroupMessageBuilder().build()
    await message.reply(**content)


@callback_handler_wrapper
async def join_group_manually_handler(message: types.Message) -> None:
    container = get_container()
    group_repository = container.resolve(IGroupRepository)

    content = await JoinGroupManuallyMessageBuilder(
        group_repository=group_repository,
    ).build()
    await message.reply(**content)


@callback_handler_wrapper
async def join_group_randomly_handler(message: types.Message) -> None:
    content = JoinGroupRandomlyMessageBuilder().build()
    await message.reply(**content)
