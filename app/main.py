import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from settings import settings

from handlers import search_router


async def main(dispatcher: Dispatcher, bot_instance: Bot):

    await dispatcher.start_polling(bot_instance, skip_updates=True)


if __name__ == "__main__":
    bot = Bot(
        token=settings.tg_token.get_secret_value(),
        parse_mode=ParseMode.HTML,
    )
    dp = Dispatcher()
    dp.include_routers(search_router)
    asyncio.run(main(dp, bot))
