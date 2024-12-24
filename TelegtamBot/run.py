import asyncio
from aiogram import Bot, Dispatcher
from App.halndlers import router
import os
from dotenv  import load_dotenv
async def main():
    load_dotenv()
    # Токен для создания бота
    bot = Bot(token=os.getenv("TOKEN"))  # это билд самый первый
    # потом будет находиться в другом файле
    dis = Dispatcher()
    dis.include_router(router=router)
    await  dis.start_polling(bot)


if __name__ == '__main__':

    try:
        print("Бот включен")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Выход")

    try:
        asyncio.run(main())
    except RuntimeError:
        print("Бот выключен")