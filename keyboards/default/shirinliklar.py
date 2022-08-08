from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shirinliklar_buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Tort'),
            KeyboardButton(text="Pirog"),
        ],
        [
            KeyboardButton(text='Musqaymoq'),
            KeyboardButton(text='Nimadir'),
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ], 
    resize_keyboard=True
)