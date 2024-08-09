import logging

from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart, Command

from bot.handlers.add_to_group import (
    add_group_manually_handler,
    add_group_randomly_handler,
    start_add_group_handler,
)
from bot.middlewares import GetOrCreateUserMiddleware
from src.bot.handlers.start_handler import start_handler
from src.bot.views import TelegramWebhookView
from src.core.configs import settings


logger = logging.getLogger(__name__)


def add_middlewares(dispatcher: Dispatcher) -> None:
    dispatcher.message.middleware(GetOrCreateUserMiddleware())
    dispatcher.callback_query.middleware(GetOrCreateUserMiddleware())


def add_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.message.register(start_handler, CommandStart())
    dispatcher.callback_query.register(start_handler, F.data == "start")

    dispatcher.callback_query.register(start_add_group_handler, F.data == "group")
    dispatcher.message.register(start_add_group_handler, Command("group"))

    dispatcher.callback_query.register(
        add_group_manually_handler,
        F.data == "add_group_manually",
    )
    dispatcher.message.register(
        add_group_manually_handler,
        Command("add_group_manually"),
    )

    dispatcher.callback_query.register(
        add_group_randomly_handler,
        F.data == "add_group_randomly",
    )
    dispatcher.message.register(
        add_group_randomly_handler,
        Command("add_group_randomly"),
    )


async def telegram_view_factory() -> TelegramWebhookView:
    bot = Bot(token=settings.BOT_TOKEN)
    await bot.set_webhook(settings.TELEGRAM_WEB_HOOK)

    dispatcher = Dispatcher()
    add_handlers(dispatcher=dispatcher)
    add_middlewares(dispatcher=dispatcher)

    return TelegramWebhookView(dispatcher=dispatcher, bot=bot)
