import logging

from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart

from src.bot.handlers.start_handler import start_handler
from src.bot.views import TelegramWebhookView
from src.core.configs import settings


logger = logging.getLogger(__name__)


def add_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.message.register(start_handler, CommandStart())
    dispatcher.callback_query.register(start_handler, F.data == "start")


async def telegram_view_factory() -> TelegramWebhookView:
    bot = Bot(token=settings.BOT_TOKEN)
    await bot.set_webhook(settings.TELEGRAM_WEB_HOOK)

    dispatcher = Dispatcher()
    add_handlers(dispatcher=dispatcher)
    return TelegramWebhookView(dispatcher=dispatcher, bot=bot)
