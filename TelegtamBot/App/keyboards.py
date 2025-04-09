from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Text.keybar_text import * 
keyboard_main = InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(text=text_keybar_average_rating_grop_kebar
    , callback_data="average_rating_grop")],
[InlineKeyboardButton(text=text_keybar_student_assement_kebar
    ,callback_data="student_assessment")],
[InlineKeyboardButton(text= text_keybar_homework_teacher
    ,callback_data="homework_teacher")],
[InlineKeyboardButton(text= text_keybar_homework_student
        ,callback_data="homework_student")]])
keyboard_help = InlineKeyboardMarkup(
inline_keyboard=
[[InlineKeyboardButton(text=text_kebar_video, callback_data="video_help")],
[InlineKeyboardButton(text=text_keybar_information, callback_data="information_help")]
])

keyboard_data = InlineKeyboardMarkup(
    inline_keyboard=
    [
    [InlineKeyboardButton(text=text_keybar_data_moth,callback_data="month")]
    ,[InlineKeyboardButton(text=text_keybar_data_week,callback_data="week")]
    ,[InlineKeyboardButton(text=text_keybar_data_day,callback_data="day")]
    ])

keyboard_homework = InlineKeyboardMarkup(
    inline_keyboard=
    [
    [InlineKeyboardButton(text=text_keybar_issued_homework,callback_data="issued_homework")],
    [InlineKeyboardButton(text=text_keybar_verified_homework,callback_data="verified_homework")]
    ])

keyboard_video = InlineKeyboardMarkup(
    inline_keyboard=
[
    [InlineKeyboardButton(text=text_keybar_video_what_work_bot
            ,callback_data="what work bot")],
    [InlineKeyboardButton(text=text_keybar_video_what_connect_develope
            ,callback_data="what connect developer")]
])