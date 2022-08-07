from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

fastfood_buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Lavash'),
            KeyboardButton(text="Xotdog"),
        ],

        [
            KeyboardButton(text='Donor'),
            KeyboardButton(text='Lavash 2'),
        ],

        [
            KeyboardButton(text='🏠Bosh sahifa')
        ]
    ],
    resize_keyboard=True
)
