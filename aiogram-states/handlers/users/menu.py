from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message,ReplyKeyboardRemove

from keyboards.default.EntryKeyboard import menuEntry
from keyboards.default.menuKeyboard import menu

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)

@dp.message_handler(text="Python darslari")
async def send_link(message: Message):
    await message.answer("Jonibek Dev || Python darslari: https://youtu.be/Ka6WgzC-Omo")

@dp.message_handler(text="Entry darslari")
async def send_link(message: Message):
    await message.answer("Entry darslar ro'yhati", reply_markup=menuEntry)

@dp.message_handler(text="#00 Dars")
async def send_link(message: Message):
    await message.answer("Entry darslari https://youtu.be/-QIc9cXiFXU?list=PLSDz7RX2s66fB7zrc-UwYNhVquhPNi2Q2")

@dp.message_handler(text="#01 Dars")
async def send_link(message: Message):
    await message.answer("Entry darslari https://www.youtube.com/watch?v=Prz5u6XJYG4&list=PLSDz7RX2s66fB7zrc-UwYNhVquhPNi2Q2&index=2&pp=gAQBiAQB")

@dp.message_handler(text="#02 Dars")
async def send_link(message: Message):
    await message.answer("Entry darslari https://www.youtube.com/watch?v=x_ovY30VW5g&list=PLSDz7RX2s66fB7zrc-UwYNhVquhPNi2Q2&index=3&pp=gAQBiAQB")


@dp.message_handler(text="Ortga")
async def send_link(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=ReplyKeyboardRemove())

