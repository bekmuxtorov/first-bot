from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

toamlar_buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Osh'),
            KeyboardButton(text="Sho'rva"),
        ],

        [
            KeyboardButton(text='Monti'),
            KeyboardButton(text='Chuchvara'),
        ],

        [
            KeyboardButton(text='🏠Bosh sahifa')
        ]


    ],
    resize_keyboard=True
)
