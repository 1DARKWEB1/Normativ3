import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio

API_TOKEN = '8199528786:AAGNvFfO_r8zgdWNSZQi3gmV1GpdrYpNRMQ'
API_URL = 'http://127.0.0.1:8000/api/courses/'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def get_courses():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            return await response.json()


@dp.message(Command("start"))
async def start(message: types.Message):
    courses = await get_courses()
    buttons = [[KeyboardButton(text=course["title"])] for course in courses]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("Выберите курс:", reply_markup=keyboard)


@dp.message()
async def course_info(message: types.Message):
    courses = await get_courses()
    for course in courses:
        if course["title"] == message.text:
            subjects = course["subjects"]
            text = f"📚 {course['title']}\n\n"
            for subj in subjects:
                text += f"🔹 {subj['title']}\n{subj['description']}\n\n"
            await message.answer(text)
            break


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
