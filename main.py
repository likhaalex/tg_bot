import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Получение токена из переменных окружения
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

# Приветственное сообщение
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я твой Telegram-бот. "
                         "Давай поговорим! Чем я могу помочь? "
                         "Например, скажи 'расскажи анекдот', если хочешь, чтобы я рассказал анекдот.\n\n"
                         "Если ты не знаешь, что сказать, попробуй одну из этих команд:\n"
                         "/help - Список доступных команд и фраз\n"
                         "расскажи анекдот - Я расскажу тебе анекдот\n"
                         "как дела? - Узнаешь, как у меня дела\n"
                         "помоги мне - Я помогу тебе\n"
                         "пока - Прощание")

# Команда /help для вывода доступных фраз
@dp.message(Command('help'))
async def send_help(message: types.Message):
    await message.answer("Вот что я могу: \n\n"
                         "/help - Список команд\n"
                         "расскажи анекдот - Я расскажу тебе анекдот\n"
                         "как дела? - Узнаешь, как у меня дела\n"
                         "помоги мне - Я помогу тебе\n"
                         "пока - Прощание\n\n"
                         "Напиши любую из этих фраз, и я отреагирую!")

# Обработка всех сообщений
@dp.message()
async def handle_message(message: types.Message):
    text = message.text.lower()

    if text == 'расскажи анекдот':
        await message.answer("Вот анекдот: \n\nКакой металл самый веселый? — Смехолёт!")
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
