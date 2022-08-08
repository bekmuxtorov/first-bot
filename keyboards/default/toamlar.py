from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

toamlar_buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Osh'),
            KeyboardButton(text="Sho'rva"),
        ],
        [
            KeyboardButton(text='Manti'),
            KeyboardButton(text='Shashlik'),
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ], 
    resize_keyboard=True
)