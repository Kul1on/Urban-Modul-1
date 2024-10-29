from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

logging.basicConfig(level=logging.INFO)

# токен бота
API_TOKEN = 'сюда'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот помогающий твоему здоровью.")
    print("Привет! Я бот помогающий твоему здоровью.")  # вывод в консоль для проверки

# Обработчик для любых других сообщений
@dp.message_handler()
async def all_messages(message: types.Message):
    await message.reply("Введите команду /start, чтобы начать общение.")
    print("Введите команду /start, чтобы начать общение.")  # вывод в консоль для проверки

if __name__ == '__main__':
    print("Бот запущен и готов к работе.")
    executor.start_polling(dp, skip_updates=True)
