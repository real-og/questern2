from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts

begin_quest_kb = ReplyKeyboardMarkup([[texts.start_travel]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

hint_kb = ReplyKeyboardMarkup([[texts.get_hint]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

hint_double_kb = ReplyKeyboardMarkup([[texts.get_more_hint]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)



continue_kb = ReplyKeyboardMarkup([[texts.continue_quest]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)


hint_extended_kb = ReplyKeyboardMarkup([[texts.get_hint], [texts.hint_find_code_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

hint_location_kb = ReplyKeyboardMarkup([[texts.hint_find_code_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)
