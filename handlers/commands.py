from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.greeting)
    await message.answer(texts.ask_for_name)
    # table.sheet.append_user(str(message.from_user.id), message.from_user.username, message.from_user.full_name)
    await aiotable.append_user(str(message.from_user.id), message.from_user.username, message.from_user.full_name)
    await State.entering_name.set()

@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help_message)
