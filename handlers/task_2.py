from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table


@dp.message_handler(state=State.ended_task_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.continue_quest:
        table.sheet.change_level(str(message.from_user.id), '2')
        await message.answer(texts.name_task_2)
        await message.answer(texts.task_2_1)
        await message.answer(texts.provide_answer)
        await State.task_2_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.continue_kb)


@dp.message_handler(state=State.task_2_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_2_1_ans:
        await message.answer(texts.right_answer)
        await message.answer(texts.ask_for_continue, reply_markup=kb.continue_kb)
        await State.ended_task_2.set()
    elif input == texts.get_hint:
        await message.answer(texts.task_2_1_hint)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)