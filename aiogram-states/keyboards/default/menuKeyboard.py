from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Entry darslari"),
            KeyboardButton(text="Python darslari"),
        ],
    ],
    resize_keyboard=True

)
