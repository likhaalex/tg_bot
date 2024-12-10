import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from flask import Flask
from threading import Thread

# Получение токена из переменных окружения
TOKEN = os.getenv("TOKEN")

# Инициализация бота и диспетчера
bot = Bot(TOKEN)
dp = Dispatcher()

# Flask приложение для поддержания активности
app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

# Обработчик команды /start
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я твой Telegram-бот. Напиши мне что-нибудь, и я отвечу!")

# Обработчик всех других сообщений
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Ты написал: {message.text}", parse_mode="HTML")

# Запуск Flask приложения в отдельном потоке
def run_flask():
    app.run(host='0.0.0.0', port=80)

# Функция для запуска бота
async def main():
    print("Бот запущен!")
    # Запуск Flask в отдельном потоке
    thread = Thread(target=run_flask)
    thread.start()
    
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
