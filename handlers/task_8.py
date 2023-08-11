from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable

@dp.message_handler(state=State.ended_task_7)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.continue_quest:
        await aiotable.change_level(str(message.from_user.id), '8')
        await message.answer(texts.name_task_8)
        await message.answer(texts.task_8_1)
        await message.answer(texts.provide_answer, reply_markup=kb.hint_location_kb)
        await State.task_8_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.continue_kb)


@dp.message_handler(state=State.task_8_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() == texts.task_8_1_ans:
        await message.answer(texts.right_answer)
        await message.answer(texts.ask_for_continue, reply_markup=kb.continue_kb)
        await State.ended_task_8.set()
    elif input == texts.hint_find_code_btn:
        with open('images/print_room.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.provide_answer)
    elif input == texts.get_hint:    
        await message.answer(texts.task_8_1_hint, reply_markup=kb.hint_double_kb)
    elif input == texts.get_more_hint:
        await message.answer(texts.task_8_2_hint)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)