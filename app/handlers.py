from aiogram import Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent)
from aiogram import Bot, F, html, types
from aiogram.utils.markdown import hide_link
from yamusic import yandex_music as client
from settings import settings

search_router = Router()


def generator(url: str, title: str, artist: str) -> str:
    text = (
        f"{hide_link(url)}\n"
        f"{html.bold(html.quote(title))}\n"
        f"{html.quote(artist)}"
        )

    return text


@search_router.inline_query(F.query)
async def links(inline_query: InlineQuery):
    results = await client.track_results(inline_query.query)
    results = [
        InlineQueryResultArticle(
            id=result["id"],
            title=result["title"],
            url=result.get("url"),
            hide_url=True,
            description=result["artist"],
            thumbnail_url=result.get("cover_url"),
            thumbnail_width=50,
            thumbnail_height=50,
            input_message_content=InputTextMessageContent(
                message_text=generator(
                    result["url"], result["title"], result["artist"]
                ),
            ),
        )
        for result in results
    ]
    await inline_query.answer(results)


@search_router.message(CommandStart())
async def cmd_start(message: types.Message, bot: Bot):
    await message.answer(
        f"{bot_me.username}\n"
        f"@{bot_me.first_name}\n"
        "Commands:\n"
        "/start - start interact with bot\n"
        "/help - start interact with bot\n"
        f"Type '@{settings.bot_info[1]}' " 
        "in chat - search for music via Yandex.music"
    )


@search_router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        f"Bot help send music from {html.bold('Yandex.music')}.\n"
        "To start interact with bot "
        "type username of bot in chat.\nExample:\n"
        f"@{settings.bot_info[1]} Benny Benassi - Satisfaction",
    )
