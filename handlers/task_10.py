from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import logic
import aiotable

@dp.message_handler(state=State.ended_task_9)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.continue_quest:
        await aiotable.change_level(str(message.from_user.id), '10')
        await message.answer(texts.name_task_10)
        await message.answer(texts.task_10_1)
        await message.answer(texts.provide_answer)
        await State.task_10_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.continue_kb)


@dp.message_handler(state=State.task_10_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() == texts.task_10_1_ans:
        number = logic.increase_counter()
        await aiotable.set_lottary_number(str(message.from_user.id), number)
        await message.answer(texts.right_answer)
        await message.answer(texts.success_message)
        # await message.answer(texts.generate_num_message(number))
        await State.ended_task_10.set()
    elif input == texts.get_hint:    
        await message.answer(texts.task_10_1_hint, reply_markup=kb.hint_double_kb)
    elif input == texts.get_more_hint:
        await message.answer(texts.task_10_2_hint)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)