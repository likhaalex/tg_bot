import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ParseMode
import asyncio

# Получение токена из переменных окружения
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

# Словарь для хранения состояний пользователей
user_state = {}

# Приветственное сообщение
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я твой Telegram-бот. "
                         "Давай поговорим! Чем я могу помочь? "
                         "Например, скажи 'расскажи анекдот', если хочешь, чтобы я рассказал анекдот.")

# Обработка сообщения 'расскажи анекдот'
@dp.message()
async def echo_message(message: types.Message):
    text = message.text.lower()

    # Проверка на ключевое слово
    if text == 'расскажи анекдот':
        await message.answer("Вот анекдот: \n\nКакой металл самый веселый? — Смехолёт!")
        await message.answer("Хочешь поговорить о чем-то еще?")
        user_state[message.from_user.id] = 'waiting_for_next_message'
    elif text == 'как дела?':
        await message.answer("Все хорошо! А у тебя как?")
        user_state[message.from_user.id] = 'waiting_for_next_message'
    elif text == 'помоги мне':
        await message.answer("Как я могу помочь? Расскажи, что нужно.")
        user_state[message.from_user.id] = 'waiting_for_help_request'
    elif message.from_user.id in user_state and user_state[message.from_user.id] == 'waiting_for_help_request':
        await message.answer(f"Ты попросил помочь с: {message.text}. "
                             "Попробуй еще уточнить, что именно нужно сделать!")
        user_state[message.from_user.id] = 'waiting_for_next_message'
    else:
        await message.answer(f"Ты написал: {message.text}. Продолжай общаться, я всегда на связи!")

# Завершающий диалог
@dp.message()
async def handle_default(message: types.Message):
    if message.text.lower() == 'пока':
        await message.answer("Пока! Надеюсь, еще пообщаемся!")
        user_state[message.from_user.id] = 'waiting_for_next_message'

# Запуск бота
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

