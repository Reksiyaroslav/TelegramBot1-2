from aiogram import Router, F
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart, Command
from  aiogram.types import FSInputFile,BufferedInputFile
import App.keyboards as kb
import  App.logic as log
router = Router()
inform_text = ""

@router.message(CommandStart())
async def cmd_start(message: Message):
    await  message.answer("Hello", reply_markup=kb.keyboard_main)


@router.message(Command("hellp"))
async def hellp(message: Message):
    await  message.answer("Какие у вас вопросы ?")


@router.callback_query(F.data == 'type_subject')
async def category_log_type_subject(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали изменения темы урока ")
    await  callback.message.answer("Оправте файл")
    new_file = BufferedInputFile(file=10000, filename="file_name")
    if new_file.filename.endswith(".xlsx"):

        try:
            log.new_type_sq(new_file)

        except:
            print(f"{new_file.filename} не соответствует ожидаемому формату.")


@router.callback_query(F.data == 'average-rating-grop')
async def category_log_average_rating_grop(callback: CallbackQuery):
    await  callback.answer("Вы выбрали функцию")
    await  callback.message.answer("Вы выбрали средняя н оценка в группе")
    await  callback.message.answer("Оправте файл")
    new_file = BufferedInputFile(file= 10000,filename="file_name")
    if  new_file.filename.endswith(".xlsx"):

        try: log.new_type_sq(new_file)

        except:
            print(f"{new_file.filename} не соответствует ожидаемому формату.")

@router.message()
async def create_file(message: Message):
    await message.answer("файл получен")
    new_file = message.document
    if F.data == 'type_subject':

        if new_file.file_name.endswith(".xlsx"):

            log.new_type_sq(file=new_file.file_name, inform_text= inform_text)
            await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")

    elif F.data == 'average-rating-grop':
        if new_file.file_name.endswith(".xlsx"):
            file = FSInputFile(new_file.file_id, "Infor_file.xlsx")
            log.new_average_rating_grop(file.filename, inform_text)
            await  message.answer(inform_text)
        else:
            await  message.answer(f"Не соответствует ожидаемому формату.")
