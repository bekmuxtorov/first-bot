from cgitb import text
from aiogram import types
from keyboards.default.shirinliklar import shirinliklar_buttons
from loader import dp


# Echo bot
@dp.message_handler(text='Shirinliklar')
async def bot_echo(message: types.Message):
    await message.answer(message.text, reply_markup=shirinliklar_buttons)
