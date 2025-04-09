from aiogram import Router, F
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart, Command
from  aiogram.types import FSInputFile
import App.keyboards as kb
import App.logic as log
import  os
from Text.telegram_text_message import *
router = Router()
inform_text = ""
list_text = []
class FmsContext():
    text=""
    time=""

@router.message(CommandStart())
async def cmd_start(message: Message):
    await  message.answer(text_message_hello,
                          reply_markup=kb.keyboard_main)

@router.message(Command("help"))
async def hellp(message: Message):
    await  message.answer(text_message_porblems,
                          reply_markup=kb.keyboard_help)

@router.callback_query(F.data == 'video_help')
async def video_helps(callback: CallbackQuery):
    await  callback.answer(text_message_func_using)
    await  callback.message.answer(text_message_video_help_bot)
    await  callback.message.answer(text_message_verebal+ text_message_video_hellp_work_bot,
                                   reply_markup=kb.keyboard_video)

@router.callback_query(F.data== "information_help")
async  def text_information(callback: CallbackQuery):
    await  callback.answer(text_message_verebal)
    await  callback.message.answer(text_message_information)
    await  callback.message.answer(text_message_imformaion_help)

@router.callback_query(F.data == 'what work bot')
async def video_what_work_bot(callback: CallbackQuery):
    await  callback.answer(text_message_func_using)
    await  callback.message.answer(text_message_video_hellp_work_bot)
    video = FSInputFile('Files\\Myfiles\\Video_help.mp4')
    await callback.message.answer_video(video)

@router.callback_query(F.data == 'what connect developer')
async def video_what_connect_developer(callback: CallbackQuery):
    await  callback.answer(text_message_func_using)
    await  callback.message.answer(text_message_video_what_connect_developer)
    video = FSInputFile('Files\\Myfiles\\me_telegram.mp4')
    await callback.message.answer_video(video)

@router.callback_query(F.data == 'homework_teacher')
async def category_log_homework_teacher(callback: CallbackQuery):
    await  callback.answer(text_message_func_using)
    await  callback.message.answer(text_message_homework_teacher)
    await  callback.message.answer(text_message_verebal + text_message_varibal_homework,
                            reply_markup=kb.keyboard_homework)

@router.callback_query(F.data == 'issued_homework')
async def category_log_homework_teacher_issued(callback: CallbackQuery):
    await  callback.answer(text_message_func_using)
    await  callback.message.answer(text_message_issued_homework)
    FmsContext.text= text_message_issued_homework
    await  callback.message.answer(text_message_verebal)
    await  callback.message.answer(text_message_verebal_data,reply_markup=kb.keyboard_data)

@router.callback_query(F.data == 'verified_homework')
async def category_log_homework_teacher_verified_homework(callback: CallbackQuery):
    await  callback.answer(text_message_func_using)
    await  callback.message.answer(text_message_verified_homework)
    FmsContext.text= text_message_verified_homework
    await  callback.message.answer(text_message_func_using)
    await  callback.message.answer(text_message_verebal_data,reply_markup=kb.keyboard_data)

@router.callback_query(F.data == 'month')
async def category_log_homework_teacher_month(callback: CallbackQuery):
    await  callback.answer(text_message_time_moth)
    await  callback.message.answer(text_message_time_moth)
    FmsContext.time= text_time_moth
    await  callback.message.answer(text_message_load_fille)

@router.callback_query(F.data == 'week')
async def category_log_homework_teacher_week(callback: CallbackQuery):
    await  callback.answer(text_message_time_week)
    await  callback.message.answer(text_message_time_week)
    FmsContext.time= text_time_week
    await  callback.message.answer(text_message_load_fille)

@router.callback_query(F.data == 'day')
async def category_log_homework_teacher_day(callback: CallbackQuery):
    await  callback.answer(text_time_data_day)
    await  callback.message.answer(text_time_data_day)
    FmsContext.time= text_time_day
    await  callback.message.answer(text_message_load_fille)
@router.callback_query(F.data == 'average_rating_grop')
async def category_log_average_rating_grop(callback: CallbackQuery):
    await  callback.answer(text_message_func_using)
    await  callback.message.answer(text_message_average_rating_grop)
    FmsContext.text = text_message_average_rating_grop
    await  callback.message.answer(text_message_load_fille)

@router.callback_query(F.data == 'student_assessment')
async def category_log_student_assessment(callback: CallbackQuery):
    await  callback.answer(text_message_func_using)
    await  callback.message.answer(text_message_student_asessment)
    FmsContext.text=text_message_student_asessment
    await  callback.message.answer(text_message_load_fille)

@router.callback_query(F.data == 'homework_student')
async def category_log_student_assessment(callback: CallbackQuery):
    await  callback.answer(text_message_func_using)
    await  callback.message.answer(text_message_homeworl_student)
    FmsContext.text=text_message_homeworl_student
    await  callback.message.answer(text_message_load_fille)

@router.message()
async def create_file(message: Message):
    inform_text = FmsContext.text
    if not  os.getcwd().endswith("Files") :
        os.chdir(f"Files")
    await message.answer("файл получен")
    if not os.path.isdir(f"Files {message.from_user.id}"):
        os.mkdir(f"Files {message.from_user.id}")
    #os.chdir(f"Files {message.from_user.id}"")

    if inform_text == text_message_average_rating_grop:
        new_file = message.document
        if new_file.file_name.endswith(".xlsx"):
            list_text = log.search_average_rating_grop(file=new_file.file_name)
            inform_text = f"{list_text}"
            inform_text = inform_text.replace(',', "\n")
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("'")
            await  message.answer(inform_text)
        else:
            await  message.answer(text_error_obel)

    elif inform_text ==text_message_issued_homework:
        new_file = message.document
        if new_file.file_name.endswith(".xlsx"):
            list_text= log.search_verified_homework(new_file,FmsContext.time)
            inform_text = f"{list_text}"
            inform_text = inform_text.replace(',', "\n")
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("'")
            await  message.answer(inform_text)
        else:
            await  message.answer(text_error_obel)

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
            await  message.answer(text_error_obel)

    elif inform_text == text_message_student_asessment:
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
            await  message.answer(text_error_obel)

    elif inform_text == text_message_homeworl_student:
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
            await  message.answer(text_error_obel)

    else:
        await  message.answer(text_error)
