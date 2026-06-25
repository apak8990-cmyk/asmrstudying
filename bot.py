import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv(
    "WEB_APP_URL",
    "https://apak8990-cmyk.github.io/asmrstudying/website/",
)

if not TOKEN:
    raise RuntimeError("Set BOT_TOKEN in .env or in the environment before starting the bot.")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Start Study Session",
                    web_app=WebAppInfo(url=WEB_APP_URL),
                )
            ]
        ]
    )

    await message.answer(
        "Choose your ASMR study world",
        reply_markup=keyboard,
    )


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
