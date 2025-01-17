from aiogram import Router, F
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart, Command
from  aiogram.types import FSInputFile,BufferedInputFile
import App.keyboards as kb
import  App.logic as log
router = Router()
inform_text = ""
list_text = []
@router.message(CommandStart())
async def cmd_start(message: Message):
    await  message.answer("Здраствуйте выбирайте функцую которую вам нужно", reply_markup=kb.keyboard_main)

class FmsContext():
    text=""
    time=""

@router.message(Command("help"))
async def hellp(message: Message):
    await  message.answer("Какие у вас вопросы ?",reply_markup=kb.keyboard_help)


@router.callback_query(F.data == 'homework_teacher')
async def category_log_homework_teacher(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали посмотреть что с дз у преподователя")
    await  callback.message.answer("Теперь выберите что хотите получить :\n"
    "Выданные дз или Проверенные  дз",reply_markup=kb.keyboard_homework)

@router.callback_query(F.data == 'issued_homework')
async def category_log_homework_teacher_issued(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали узначть сколько выданно дз у преподователя")
    FmsContext.text= "Вы выбрали узнать сколько выданно дз у преподователя"
    await  callback.message.answer("Теперь выберите что хотите получить :\n"
    "За месяц  дз или За неделю дз",reply_markup=kb.keyboard_data)

@router.callback_query(F.data == 'verified_homework')
async def category_log_homework_teacher_verified_homework(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали узначть сколько провереные  дз у преподователя")
    FmsContext.text= "Вы выбрали узнать сколько проверенные  дз у преподователя"
    await  callback.message.answer("Теперь выберите что хотите получить :\n"
    "За месяц  дз или За неделю дз",reply_markup=kb.keyboard_data)

@router.callback_query(F.data == 'month')
async def category_log_homework_teacher_month(callback: CallbackQuery):
    await  callback.answer("Вы выбрали месяц")
    await  callback.message.answer("Вы выбрали месяц")
    FmsContext.time= "Месяц"
    await  callback.message.answer("Оправте файл")

@router.callback_query(F.data == 'week')
async def category_log_homework_teacher_week(callback: CallbackQuery):
    await  callback.answer("Вы выбрали неделя")
    await  callback.message.answer("Вы выбрали неделя")
    FmsContext.time= "Неделя"
    await  callback.message.answer("Оправте файл")

@router.callback_query(F.data == 'day')
async def category_log_homework_teacher_day(callback: CallbackQuery):
    await  callback.answer("Вы выбрали day")
    await  callback.message.answer("Вы выбрали day")
    FmsContext.time= "День"
    await  callback.message.answer("Оправте файл")
@router.callback_query(F.data == 'average_rating_grop')
async def category_log_average_rating_grop(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали средняя поешаемоть у преподователя")
    FmsContext.text = "Вы выбрали средняя поешаемоть у преподователя"

    await  callback.message.answer("Оправте файл")
@router.callback_query(F.data == 'student_assessment')
async def category_log_student_assessment(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали провереть успеваемоть студентов")
    FmsContext.text=("Вы выбрали провереть успеваемоть студентов")
    await  callback.message.answer("Оправте файл")
@router.callback_query(F.data == 'homework_student')
async def category_log_student_assessment(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали провереть успеваемоть студентов")
    FmsContext.text=("Вы выбрали провереть процент дз у  студентов")
    await  callback.message.answer("Оправте файл")
@router.message()
async def create_file(message: Message):
    inform_text = FmsContext.text
    await message.answer("файл получен")
    new_file = message.document
    if inform_text == "Вы выбрали средняя поешаемоть у преподователя":

        if new_file.file_name.endswith(".xlsx"):

            list_text = log.search_average_rating_grop(file=new_file)
            inform_text = f"{list_text}"
            inform_text = inform_text.replace(',', "\n")
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("'")


            await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")

    elif inform_text == "Вы выбрали узнать сколько проверенные  дз у преподователя":
        if new_file.file_name.endswith(".xlsx"):
            list_text= log.search_verified_homework(new_file,FmsContext.time)
            inform_text = f"{list_text}"
            inform_text = inform_text.replace(',', "\n")
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("'")

            await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")
    elif inform_text == "Вы выбрали узнать сколько выданно дз у преподователя":
        if new_file.file_name.endswith(".xlsx"):
            list_text= log.search_issued_homework(new_file,FmsContext.time)
            inform_text = f"{list_text}"
            inform_text = inform_text.replace(',',"\n")
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("'")
            await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")

    elif inform_text == 'Вы выбрали провереть успеваемоть студентов':
        if new_file.file_name.endswith(".xlsx"):
            file = FSInputFile(new_file.file_id, "Infor_file.xlsx")
            list_text= log.search_student_assessment(file.filename)
            inform_text = f"{list_text}"
            inform_text = inform_text.replace(',', "\n")
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("'")
            await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")
    elif inform_text == 'Вы выбрали провереть процент дз у  студентов':
        if new_file.file_name.endswith(".xlsx"):
            list_text_1 = []
            file = FSInputFile(new_file.file_id, "Infor_file.xlsx")
            list_text= log.search_percentage_of_homework_per_month(file.filename)
            if len(list_text) <50:
                list_text = log.search_issued_homework(new_file, FmsContext.time)
                inform_text = f"{list_text}"
                inform_text = inform_text.replace(',', "\n")
                inform_text = inform_text.strip("[]")
                inform_text = inform_text.strip("'")
                await  message.answer(inform_text)
            elif len(list_text) >50 and  len(list_text) <100:

                for list_len in range(0,int(len(list_text)/2)):
                    list_text_1.append(list_text[list_len])
                inform_text = f"{list_text_1}"
                inform_text = inform_text.replace(',', "\n")
                inform_text = inform_text.strip("[]")
                inform_text = inform_text.strip("'")
                await  message.answer(inform_text)
                list_text_1.clear()
                for list_len in range(int(len(list_text)/2),len(list_text)):
                    list_text_1.append(list_text[list_len])
                inform_text = f"{list_text_1}"
                inform_text = inform_text.replace(',', "\n")
                inform_text = inform_text.strip("[]")
                inform_text = inform_text.strip("'")
                await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")

    else:
        await  message.answer(f"Ошибка")
