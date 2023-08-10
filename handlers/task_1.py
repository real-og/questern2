from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable


@dp.message_handler(state=State.greeting_screen)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.start_travel:
        await aiotable.change_level(str(message.from_user.id), '1')
        await message.answer(texts.name_task_1)
        await message.answer(texts.task_1_1)
        await message.answer(texts.provide_answer)
        await State.task_1_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.begin_quest_kb)


@dp.message_handler(state=State.task_1_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_1_1_ans:
        await message.answer(texts.right_answer)
        await message.answer(texts.ask_for_continue, reply_markup=kb.continue_kb)
        await State.ended_task_1.set()
    elif input == texts.get_hint:
        await message.answer(texts.task_1_1_hint, reply_markup=kb.hint_double_kb)
    elif input == texts.get_more_hint:
        await message.answer(texts.task_1_2_hint)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)

