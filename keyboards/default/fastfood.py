
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

fastfood_buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Lavash'),
            KeyboardButton(text="Donor"),
        ],
        [
            KeyboardButton(text='NImadir'),
            KeyboardButton(text='Birnarsa'),
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ], 
    resize_keyboard=True
)