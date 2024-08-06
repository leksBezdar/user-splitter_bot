import logging

from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart

from src.bot.handlers.start_handler import start_handler
from src.bot.views import TelegramWebhookView
from src.core.configs import settings


logger = logging.getLogger(__name__)


def add_handlers(dp: Dispatcher) -> None:
    dp.message.register(start_handler, CommandStart())
    dp.callback_query.register(start_handler, F.data == "Start")


async def telegram_view_factory() -> TelegramWebhookView:
    bot = Bot(token=settings.BOT_TOKEN)
    await bot.set_webhook(settings.TELEGRAM_WEB_HOOK)

    dp = Dispatcher()
    add_handlers(dp=dp)
    return TelegramWebhookView(dispatcher=dp, bot=bot)