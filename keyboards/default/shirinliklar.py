from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shirinliklar_buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="To'rt"),
            KeyboardButton(text="Pirog"),
        ],

        [
            KeyboardButton(text='Musqaymoq'),
            KeyboardButton(text='Chuchvara'),
        ],

        [
            KeyboardButton(text='🏠Bosh sahifa')
        ]
    ],
    resize_keyboard=True
)
