from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ichimliklar_buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Pepsi'),
            KeyboardButton(text="Cola"),
        ],

        [
            KeyboardButton(text='Fanta'),
            KeyboardButton(text='Choy'),
        ],

        [
            KeyboardButton(text='🏠Bosh sahifa')
        ]
    ],
    resize_keyboard=True
)
