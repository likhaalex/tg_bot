import os
import random
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

# Получение токенов из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CAT_API_KEY = os.getenv("CAT_API_KEY")

bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher()

# Словарь для хранения состояний пользователей
user_state = {}

# Приветственное сообщение
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я твой Telegram-бот. "
                         "Давай поговорим! Чем я могу помочь?\n\n"
                         
                         "/help - Список доступных команд и фраз\n")

# Получение случайной фотографии кошки через API
async def get_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        'x-api-key': CAT_API_KEY  # Ваш ключ API
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            if response.status == 200 and data:
                return data[0]["url"]
            else:
                return None

# Команда /help для вывода доступных фраз
@dp.message(Command('help'))
async def send_help(message: types.Message):
    await message.answer("Вот что я могу: \n\n"
                         "/help - Список команд\n"
                         "Покажи кошку - Я покажу тебе фото кошки\n"
                         "Как дела? - Узнаешь, как у меня дела\n"
                         "Помоги мне - Я помогу тебе\n"
                         "Пока - Прощание\n\n"
                         "Напиши любую из этих фраз, и я отреагирую!")

# Обработка сообщения 'покажи кошку'
@dp.message()
async def handle_message(message: types.Message):
    text = message.text.lower()

    # Проверка на ключевое слово
    if text == 'покажи кошку':
        cat_image_url = await get_cat_image()
        if cat_image_url:
            await message.answer_photo(cat_image_url, caption="Вот твоя кошка!")
        else:
            await message.answer("Не удалось найти кошку. Попробуй позже.")
    elif text == 'как дела?':
        await message.answer("Все хорошо! А у тебя как?")
    elif text == 'помоги мне':
        await message.answer("Как я могу помочь? Расскажи, что нужно.")
    elif text == 'пока':
        await message.answer("Пока! Надеюсь, еще пообщаемся!")
    else:
        await message.answer(f"Ты написал: {message.text}. Продолжай общаться, я всегда на связи!")

# Запуск бота
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
