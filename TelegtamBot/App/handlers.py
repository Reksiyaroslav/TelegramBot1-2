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
    await  message.answer("Hello", reply_markup=kb.keyboard_main)



@router.message(Command("help"))
async def hellp(message: Message):
    await  message.answer("Какие у вас вопросы ?",reply_markup=kb.keyboard_help)


@router.callback_query(F.data == 'type_subject')
async def category_log_type_subject(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали изменения темы урока ")
    await  callback.message.answer("Оправте файл")







@router.callback_query(F.data == 'average_rating_grop')
async def category_log_average_rating_grop(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали средняя н оценка в группе")
    await  callback.message.answer("Оправте файл")








@router.message()
async def create_file(message: Message):

    await message.answer("файл получен")
    new_file = message.document

    if F.data == 'type_subject':

        if new_file.file_name.endswith(".xlsx"):

            list_text = log.search_average_rating_grop(file=new_file)
            inform_text = f"{list_text}"
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip(",")
            inform_text = inform_text.strip("''")
            


            await  message.answer(inform_text)





        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")

    elif F.data == 'average_rating_grop':
        if new_file.file_name.endswith(".xlsx"):
            file = FSInputFile(new_file.file_id, "Infor_file.xlsx")
            list_text= log.search_average_rating_grop(file.filename)

            inform_text = f"{list_text}"
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("''")
            inform_text = inform_text.strip(",")
            await  message.answer(inform_text)

    elif F.data == 'average_rating_grop':
        if new_file.file_name.endswith(".xlsx"):
            file = FSInputFile(new_file.file_id, "Infor_file.xlsx")
            list_text= log.search_student_assessment(file.filename)

            inform_text = f"{list_text}\n"
            inform_text = inform_text.strip("[]")
            inform_text = inform_text.strip("''")
            inform_text = inform_text.strip(",")
            await  message.answer(inform_text)




    else:
        await  message.answer(f"Не соответствует ожидаемому формату.")
