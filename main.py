#Добавление token через .env
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'token.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print(" Файл token.env не найден!")

#логика бота
import asyncio 
from aiogram import Bot, Dispatcher 
from aiogram import F 
from aiogram.filters import Command 
from aiogram.types import Message,CallbackQuery 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
 
TOKEN = os.getenv("BOT_TOKEN")
user_ids = set() 

bot = Bot(token=TOKEN) 
dp = Dispatcher() 

#Добавление пользователя к рассылке
@dp.message(Command("start")) 
async def command_start_handler(message: Message): 
  await message.answer("Теперь вы будете получать информацию с сервисов")
  user_ids.add(message.chat.id)

#Рассылка о ошибке 1 аргумент - название проекта; 2 аргумент - log ошибки
async def alert(project,error_log):
   count=0
   for user_id in user_ids:
        try:
            await bot.send_message(user_id, f"{project} : {error_log}")
            count += 1
        except Exception as e:
            print(f"Не удалось отправить {user_id}: {e}")

 
async def main(): 
  await dp.start_polling(bot) 
 
if __name__ == "__main__": 

  asyncio.run(main())
