from cgitb import text
from aiogram import types
from loader import dp
from keyboards.default.ichimliklar import ichimliklar_buttons

# Echo bot
@dp.message_handler(text='Ichimliklar')
async def bot_echo(message: types.Message):
    await message.answer(text='Ichimliklardan tanlang: ', reply_markup=ichimliklar_buttons)
