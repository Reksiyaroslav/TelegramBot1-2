from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard_main = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Замена тему", callback_data="type_subject")],
                     [InlineKeyboardButton(text="Средняя оценка группы", callback_data="average_rating_grop")]
                     ,[InlineKeyboardButton(text="Оценки студентов ", callback_data="student_assessment")],
                     [InlineKeyboardButton(text="Проверка дз у преподователя", callback_data="homework_teacher")]])
keyboard_help = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text= "Видео", callback_data="video_help")],
                    [InlineKeyboardButton(text= "Информация", callback_data="information_help")]])

keyboard_data = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Месяц",callback_data="month")]
    ,[InlineKeyboardButton(text="Неделя",callback_data="week")]
    ,[InlineKeyboardButton(text="День",callback_data="day")]])
keyboard_homework = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Выданные дз ",callback_data="issued_homework")],
    [InlineKeyboardButton(text="Проверенные  дз ",callback_data="verified_homework")]])