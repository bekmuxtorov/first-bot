from aiogram import types
from loader import dp
from keyboards.default.menu import menu_buttons

@dp.message_handler(text='🏠Bosh sahifa')
async def bot_echo(message: types.Message):
    await message.answer(message.text, reply_markup=menu_buttons)