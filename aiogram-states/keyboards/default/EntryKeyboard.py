from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuEntry = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="#00 Dars"),
            KeyboardButton(text="#01 Dars"),
            KeyboardButton(text="#02 Dars"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ],

    ],
    resize_keyboard=True
)