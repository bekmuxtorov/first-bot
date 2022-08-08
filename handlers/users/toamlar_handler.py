from aiogram import types
from keyboards.default.toamlar import toamlar_buttons
from loader import dp


# Echo bot
@dp.message_handler(text='Toamlar')
async def bot_echo(message: types.Message):
    await message.answer(message.text, reply_markup=toamlar_buttons)
