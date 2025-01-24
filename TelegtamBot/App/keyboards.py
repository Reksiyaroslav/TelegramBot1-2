from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard_main = InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(text="Средняя посещаемость у преподавателя"
    , callback_data="average_rating_grop")],
[InlineKeyboardButton(text="Оценки студентов "
    ,callback_data="student_assessment")],
[InlineKeyboardButton(text="Проверка дз у преподавателя"
    ,callback_data="homework_teacher")],
[InlineKeyboardButton(text="Проверка процента дз у студента"
        ,callback_data="homework_student")]])
keyboard_help = InlineKeyboardMarkup(
inline_keyboard=
[[InlineKeyboardButton(text= "Видео", callback_data="video_help")],
[InlineKeyboardButton(text= "Информация", callback_data="information_help")]
])

keyboard_data = InlineKeyboardMarkup(
    inline_keyboard=
    [
    [InlineKeyboardButton(text="Месяц",callback_data="month")]
    ,[InlineKeyboardButton(text="Неделя",callback_data="week")]
    ,[InlineKeyboardButton(text="День",callback_data="day")]
    ])

keyboard_homework = InlineKeyboardMarkup(
    inline_keyboard=
    [
    [InlineKeyboardButton(text="Выданные дз ",callback_data="issued_homework")],
    [InlineKeyboardButton(text="Проверенные дз ",callback_data="verified_homework")]
    ])

keyboard_video = InlineKeyboardMarkup(
    inline_keyboard=
[
    [InlineKeyboardButton(text="Как работать с ботом?"
            ,callback_data="what work bot")],
    [InlineKeyboardButton(text="Как связаться с разработчикам?"
            ,callback_data="what connect developer")]
])