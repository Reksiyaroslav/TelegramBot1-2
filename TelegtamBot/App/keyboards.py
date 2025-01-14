from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard_main = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Замена тему", callback_data="type_subject")],
                     [InlineKeyboardButton(text="Средняя оценка группы", callback_data="average_rating_grop")]])
keyboard_help = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text= "Видео", callback_data="video_help")],
                    [InlineKeyboardButton(text= "Информация", callback_data="information_help")]])