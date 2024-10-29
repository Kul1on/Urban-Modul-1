from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import logging

logging.basicConfig(level=logging.INFO)

# Токен
API_TOKEN = 'сюда'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

class UserState(StatesGroup):
    age = State()  # Состояние для возраста
    growth = State()  # Состояние для роста
    weight = State()  # Состояние для веса

# Создаем клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard.add(button_calculate, button_info)

# Создаем Inline-клавиатуру
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я помогу вам рассчитать норму калорий.\n"
                         "Выберите опцию:", reply_markup=keyboard)

@dp.message_handler(Text(equals='Рассчитать', ignore_case=True))
async def main_menu(message: types.Message):
    await message.reply("Выберите опцию:", reply_markup=inline_keyboard)

@dp.callback_query_handler(Text(equals='formulas'))
async def get_formulas(call: types.CallbackQuery):
    await call.message.reply("Формула Миффлина-Сан Жеора:\n"
                             "Для мужчин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n"
                             "Для женщин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161")

@dp.callback_query_handler(Text(equals='calories'))
async def set_age(call: types.CallbackQuery):
    await call.message.reply("Введите свой возраст:")
    await UserState.age.set()  # Устанавливаем состояние для возраста

# Обработчик ввода возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if message.text.isdigit() and int(message.text) > 0:  # Проверка на положительное число
        await state.update_data(age=int(message.text))
        await message.reply("Введите свой рост (в см):")
        await UserState.growth.set()
    else:
        await message.reply("Пожалуйста, введите корректный возраст (положительное число).")

# Обработчик ввода роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if message.text.isdigit() and int(message.text) > 0:  # Проверка на положительное число
        await state.update_data(growth=int(message.text))
        await message.reply("Введите свой вес (в кг):")
        await UserState.weight.set()
    else:
        await message.reply("Пожалуйста, введите корректный рост (положительное число).")

# Обработчик ввода веса и расчета калорий
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

# Обработчик для кнопки "Информация"
@dp.message_handler(Text(equals='Информация', ignore_case=True))
async def info(message: types.Message):
    await message.reply("Я бот, который помогает рассчитывать норму калорий в зависимости от ваших параметров тела.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
