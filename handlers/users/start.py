from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu_buttons
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alekum, {message.from_user.full_name.title()}!\n\nBotga istalgan ingliz tilidagi so'zni kiritishingiz mumkin, men uni o'zbek tiliga tarjima qilib beraman.", reply_markup=menu_buttons)

@dp.message_handler(commands='boshlash')
async def bot_start(message: types.Message):
    await message.answer(f"Hurmatli {message.from_user.full_name.title()} Bot ishga tushdi, bemalol ishlatoring.")
