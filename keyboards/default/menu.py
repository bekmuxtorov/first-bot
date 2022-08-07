from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Toamlar'),
            KeyboardButton(text='Shirinliklar'),
        ],
        [
            KeyboardButton(text='Fastfood'),
            KeyboardButton(text='Ichimliklar')
        ],

        [
            KeyboardButton(text='Joylashuv', request_location=True),
            KeyboardButton(text='Kontakt', request_contact=True)
        ]

    ],
    resize_keyboard=True
)