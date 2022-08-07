from cgitb import text
from aiogram import types
from loader import dp
from keyboards.default.shirinliklar import shirinliklar_buttons

# Echo bot
@dp.message_handler(text='Shirinliklar')
async def bot_echo(message: types.Message):
    await message.answer(text='Taomlardan tanlang: ', reply_markup=shirinliklar_buttons)
