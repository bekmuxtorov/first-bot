from cgitb import text
from aiogram import types
from loader import dp
from keyboards.default.fastfood import fastfood_buttons

# Echo bot
@dp.message_handler(text='Fastfood')
async def bot_echo(message: types.Message):
    await message.answer(text='Fastfooddan tanlang: ', reply_markup=fastfood_buttons)
