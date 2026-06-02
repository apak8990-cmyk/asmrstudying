import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "8730112261:AAF4MHg6lCM1DIlMoWGKXI127mLImuKE2gA"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardBuilder()

    kb.button(
        text="🎧 Open Study Room",
        web_app=WebAppInfo(
            url="https://YOUR-WEBSITE-URL"
        )
    )

    await message.answer(
        "Welcome to ASMR Studying!",
        reply_markup=kb.as_markup()
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())