from aiogram import Bot
import asyncio
from settings import settings


async def get_info(bot: Bot, telegram_token: str):
    bot_me = await bot.get_me()
    await bot.close()
    with open(".env", mode="w+", encoding="UTF-8") as f:
        f.write(f"TG_TOKEN={telegram_token}")
        f.write(f"BOT_NAME={bot_me.username}\n")
        f.write(f"BOT_FIRST_NAME={bot_me.first_name}")
        f.close()


async def main():
    telegram_token = input('Please, enter ID of bot:')
    bot = Bot(
        token=telegram_token,
    )
    task = asyncio.create_task(get_info(bot, telegram_token))
    await task


asyncio.run(main())
