from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable

@dp.message_handler(state=State.ended_task_5)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.continue_quest:
        await aiotable.change_level(str(message.from_user.id), '6')
        await message.answer(texts.name_task_6)
        await message.answer(texts.task_6_1)
        await message.answer(texts.provide_answer, reply_markup=kb.hint_location_kb)
        await State.task_6_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.continue_kb)


@dp.message_handler(state=State.task_6_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() == texts.task_6_1_ans:
        with open('images/brick.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.right_answer)
        await message.answer(texts.ask_for_continue, reply_markup=kb.continue_kb)
        await State.ended_task_6.set()
    elif input == texts.hint_find_code_btn:
        with open('images/coffe.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.provide_answer)
    elif input == texts.get_hint:
        await message.answer(texts.task_6_1_hint)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)