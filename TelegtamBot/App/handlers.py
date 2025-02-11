from aiogram import Router, F
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart, Command
from  aiogram.types import FSInputFile
import App.keyboards as kb
import App.logic as log
import  os
router = Router()
inform_text = ""
list_text = []
class FmsContext():
    text=""
    time=""

@router.message(CommandStart())
async def cmd_start(message: Message):
    await  message.answer("Здравствуйте выберете функцию которую вам нужно",
                          reply_markup=kb.keyboard_main)

@router.message(Command("help"))
async def hellp(message: Message):
    await  message.answer("Какие у вас вопросы ?",
                          reply_markup=kb.keyboard_help)

@router.callback_query(F.data == 'video_help')
async def video_helps(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали видео помощи с ботам")
    await  callback.message.answer("Теперь выберите что хотите получить :\n"
    "Как работа с ботом? или Как связаться с разработчикам",
                                   reply_markup=kb.keyboard_video)

@router.callback_query(F.data== "information_help")
async  def text_information(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали получить информационный текс ")
    await  callback.message.answer("""Здравствуй пользователь, 
в данном сообщение мой создатель Reksi_D хотел бы показать 
инструкцию по эксплуатации меня. \n
Он вложил очень много усилий и времени на мою разработку. \n
Не могу не отметить, что мы крайне признательны за то, что вы 
используете именно нас. 
Теперь же, как мною пользоваться: \n
1.Нажмите на кнопку с задачей.\n
2. Отправьте Microsoft Excel файл.\n
3.Наслаждайтесь отсортированной для вас информацией!\n
Если у вас возникли какие-либо вопросы или вы нашли ошибку, просьба"
связаться с создателем в телеграмме:@Rexsi_D \n
Отличного дня!""")

@router.callback_query(F.data == 'what work bot')
async def video_what_work_bot(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали как работает бот")
    video = FSInputFile('Files\\Myfiles\\Video_help.mp4')
    await callback.message.answer_video(video)

@router.callback_query(F.data == 'what connect developer')
async def video_what_connect_developer(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали как найти разработчика ")
    video = FSInputFile('Files\\Myfiles\\me_telegram.mp4')
    await callback.message.answer_video(video)

@router.callback_query(F.data == 'homework_teacher')
async def category_log_homework_teacher(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали посмотреть что с дз у преподавателя")
    await  callback.message.answer("Теперь выберите что хотите получить :\n"
    "Выданные дз или Проверенные дз",
                            reply_markup=kb.keyboard_homework)

@router.callback_query(F.data == 'issued_homework')
async def category_log_homework_teacher_issued(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали узнать сколько выдано дз у преподавателя")
    FmsContext.text= "Вы выбрали узнать сколько выдано дз у преподавателя"
    await  callback.message.answer("Теперь выберите что хотите получить:")
    await  callback.message.answer("За месяц дз или За неделю дз",reply_markup=kb.keyboard_data)

@router.callback_query(F.data == 'verified_homework')
async def category_log_homework_teacher_verified_homework(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали узнать сколько проверенные дз у преподователя")
    FmsContext.text= "Вы выбрали узнать сколько проверенные дз у преподавателя"
    await  callback.message.answer("Теперь выберите что хотите получить:")
    await  callback.message.answer("За месяц дз или За неделю дз",reply_markup=kb.keyboard_data)

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
    await  callback.message.answer("Оправте файл"
                                   )
@router.callback_query(F.data == 'average_rating_grop')
async def category_log_average_rating_grop(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали средняя посещаемость у преподавателя")
    FmsContext.text = "Вы выбрали средняя посещаемость у преподавателя"
    await  callback.message.answer("Оправте файл")

@router.callback_query(F.data == 'student_assessment')
async def category_log_student_assessment(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали проверить успеваемость студентов")
    FmsContext.text="Вы выбрали проверить успеваемость студентов"
    await  callback.message.answer("Оправте файл")

@router.callback_query(F.data == 'homework_student')
async def category_log_student_assessment(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали проверить успеваемость студентов")
    FmsContext.text="Вы выбрали проверить процент дз у студентов"
    await  callback.message.answer("Оправте файл")

@router.message()
async def create_file(message: Message):
    inform_text = FmsContext.text
    if not  os.getcwd().endswith("Files") :
        os.chdir(f"Files")
    await message.answer("файл получен")
    if not os.path.isdir(f"Files {message.from_user.id}"):
        os.mkdir(f"Files {message.from_user.id}")
    #os.chdir(f"Files {message.from_user.id}"")

    if inform_text == "Вы выбрали средняя посещаемость у преподавателя":
        new_file = message.document
        if new_file.file_name.endswith(".xlsx"):
            list_text = log.search_average_rating_grop(file=new_file.file_name)
            inform_text = f"{list_text}"
            inform_text = inform_text.replace(',', "\n")
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("'")
            await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")

    elif inform_text == "Вы выбрали узнать сколько проверенные дз у преподавателя":
        new_file = message.document
        if new_file.file_name.endswith(".xlsx"):
            list_text= log.search_verified_homework(new_file,FmsContext.time)
            inform_text = f"{list_text}"
            inform_text = inform_text.replace(',', "\n")
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("'")
            await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")

    elif inform_text == "Вы выбрали узнать сколько выдано дз у преподавателя":
        new_file = message.document
        if new_file.file_name.endswith(".xlsx"):
            list_text= log.search_issued_homework(new_file,FmsContext.time)
            inform_text = f"{list_text}"
            inform_text = inform_text.replace(',',"\n")
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("'")
            await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")

    elif inform_text == 'Вы выбрали проверить успеваемость студентов':
        new_file = message.document
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

    elif inform_text == 'Вы выбрали проверить процент дз у студентов':
        new_file = message.document
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
