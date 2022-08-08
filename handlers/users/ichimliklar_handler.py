from cgitb import text
from aiogram import types
from keyboards.default.ichimliklar import ichimliklar_buttons
from loader import dp


# Echo bot
@dp.message_handler(text='Ichimliklar')
async def bot_echo(message: types.Message):
    await message.answer(message.text, reply_markup=ichimliklar_buttons)
