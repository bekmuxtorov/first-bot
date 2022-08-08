from cgitb import text
from aiogram import types
from keyboards.default.fastfood import fastfood_buttons
from loader import dp


# Echo bot
@dp.message_handler(text='FastFood')
async def bot_echo(message: types.Message):
    await message.answer(message.text, reply_markup=fastfood_buttons)
