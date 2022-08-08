from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ichimliklar_buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Pepsi'),
            KeyboardButton(text="Fanta"),
        ],
        [
            KeyboardButton(text='Cola'),
            KeyboardButton(text='Choy'),
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ], 
    resize_keyboard=True
)