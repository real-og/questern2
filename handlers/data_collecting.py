from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table

@dp.message_handler(state=State.entering_name)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    table.sheet.change_name(str(message.from_user.id), input)
    await message.answer(texts.ask_for_email)
    await State.entering_email.set()

@dp.message_handler(state=State.entering_email)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    table.sheet.change_email(str(message.from_user.id), input)
    await message.answer(texts.ask_for_beginning, reply_markup=kb.begin_quest_kb)
    await State.greeting_screen.set()