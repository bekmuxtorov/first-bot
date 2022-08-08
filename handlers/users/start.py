from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu_buttons
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alekum, {message.from_user.full_name}!", reply_markup=menu_buttons)

@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(message.text, reply_markup=menu_buttons)
