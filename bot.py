from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
import asyncio

TOKEN = "8730112261:AAF4MHg6lCM1DIlMoWGKXI127mLImuKE2gA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✨ Start Study Session",
                    web_app=WebAppInfo(
                        url="https://apak8990-cmyk.github.io/asmrstudying/website/"
                    )
                )
            ]
        ]
    )

    await message.answer(
        "Choose your ASMR study world ✨",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())