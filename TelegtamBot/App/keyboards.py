from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard_main = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Замена тему", callback_data="type_subject")],
                     [InlineKeyboardButton(text="Средняя оценка группы", callback_data="average-rating-grop")]])
