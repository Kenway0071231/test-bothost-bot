import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Получаем токен
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("❌ Нет токена! Добавь BOT_TOKEN в настройках bothost.ru")
    exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("✅ Тестовый бот работает на bothost.ru!")

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

async def main():
    logger.info("🚀 Бот запускается...")
    logger.info(f"Токен: {BOT_TOKEN[:10]}...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
