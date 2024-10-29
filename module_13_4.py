from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import logging


logging.basicConfig(level=logging.INFO)

# токен
API_TOKEN = 'сюда'


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

class UserState(StatesGroup):
    age = State()  # Состояние для возраста
    growth = State()  # Состояние для роста
    weight = State()  # Состояние для веса

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я помогу вам рассчитать норму калорий.\n"
                         "Введите 'Calories', чтобы начать.")

@dp.message_handler(Text(equals='Calories', ignore_case=True), state='*')
async def set_age(message: types.Message):
    await message.reply("Введите свой возраст:")
    await UserState.age.set()  # Устанавливаем состояние для возраста

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if message.text.isdigit() and int(message.text) > 0:  # Проверка на положительное число
        await state.update_data(age=int(message.text))
        await message.reply("Введите свой рост (в см):")
        await UserState.growth.set()
    else:
        await message.reply("Пожалуйста, введите корректный возраст (положительное число).")

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if message.text.isdigit() and int(message.text) > 0:  # Проверка на положительное число
        await state.update_data(growth=int(message.text))
        await message.reply("Введите свой вес (в кг):")
        await UserState.weight.set()
    else:
        await message.reply("Пожалуйста, введите корректный рост (положительное число).")

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if message.text.isdigit() and int(message.text) > 0:  # Проверка на положительное число
        await state.update_data(weight=int(message.text))

        data = await state.get_data()
        age = data['age']
        growth = data['growth']
        weight = data['weight']

        # Формула Миффлина - Сан Жеора
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
        await message.reply(f"Ваша дневная норма калорий: {calories} ккал")
        await state.finish()
    else:
        await message.reply("Пожалуйста, введите корректный вес (положительное число).")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
