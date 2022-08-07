from aiogram import types
from googletrans import Translator

from loader import dp


tarjimon = Translator()
@dp.message_handler()
async def bot_echo(message: types.Message):
    which_lang = tarjimon.detect(text=message.text).lang
    if which_lang == 'en':
        translate_uz = tarjimon.translate(text=message.text, dest='uz', src='en').text
        javob = f"""{message.text} -- {translate_uz}\n\nyozuvchi: @asadbek_muxtorov"""
        await message.answer(text=javob)




