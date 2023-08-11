from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable

@dp.message_handler(state=State.ended_task_3)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.continue_quest:
        await aiotable.change_level(str(message.from_user.id), '4')
        await message.answer(texts.name_task_4)
        await message.answer(texts.task_4_1)
        await message.answer(texts.provide_answer, reply_markup=kb.hint_location_kb)
        await State.task_4_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.continue_kb)


@dp.message_handler(state=State.task_4_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_4_1_ans:
        await message.answer(texts.right_answer)
        await message.answer(texts.ask_for_continue, reply_markup=kb.continue_kb)
        await State.ended_task_4.set()
    elif input == texts.hint_find_code_btn:
        with open('images/label.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.provide_answer)
    elif input.upper() in texts.task_4_1_ans_wrong:
        await message.answer(texts.task_4_1_correction)
    elif input == texts.get_hint:
        await message.answer(texts.task_4_1_hint)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)