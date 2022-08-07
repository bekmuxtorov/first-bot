from cgitb import text
from aiogram import types
from loader import dp
from keyboards.default.taomlar import toamlar_buttons
from keyboards.default.menu import menu_buttons


# Echo bot
@dp.message_handler(text='Toamlar')
async def bot_echo(message: types.Message):
    await message.answer(text='Taomlardan tanlang: ', reply_markup=toamlar_buttons)



