import asyncio
from aiogram import Bot, Dispatcher
from App.handlers import router
import os
from dotenv  import load_dotenv
from tkinter import Tk, Label
from tkinter import ttk,PhotoImage
# перехода в директорию
os.chdir("TelegtamBot")
async def main():
    # полуни данных 
    load_dotenv()
    # вклюни бота 
    bot = Bot(token=os.getenv("TOKEN"))
    dis = Dispatcher()
    dis.include_router(router=router)
    await  dis.start_polling(bot)
    
if __name__ == '__main__':
    
    try:
        print("Бот включен")
        root = Tk()
        root.title("Q-Cod")
        
        root.geometry("250x200") 
       

        asyncio.run(main())
    except KeyboardInterrupt:
        print("Выход")

    try:
        asyncio.run(main())
    except RuntimeError:
        print("Бот выключен")