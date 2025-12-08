import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8096671270:AAE9sgF1Ia3vEiSCqWy4x48pIBsYF9YEwJs"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# ===== Функція отримання ціни =====
async def get_price(symbol):
    symbol = symbol.lower()

    mapping = {
        "ton": "the-open-network",
        "btc": "bitcoin",
        "eth": "ethereum"
    }

    coin_id = mapping.get(symbol)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()

            if coin_id in data:
                return data[coin_id]["usd"]

    return None


# ===== Старт =====
@dp.message(Command("start"))
async def start(message: types.Message):

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💎 TON")],
            [KeyboardButton(text="💲 BTC")],
            [KeyboardButton(text="🌙 ETH")],
        ],
        resize_keyboard=True,       # робить кнопки великі та зручні
        one_time_keyboard=False    # не ховає після натискання
    )

    await message.answer("Вибери криптовалюту:", reply_markup=keyboard)


# ===== Натискання на ВЕЛИКІ кнопки =====
@dp.message()
async def handle_buttons(message: types.Message):

    text = message.text.strip().lower()

    if text == "💎 ton" or text == "ton":
        price = await get_price("ton")
    elif text == "💲 btc" or text == "btc":
        price = await get_price("btc")
    elif text == "🌙 eth" or text == "eth":
        price = await get_price("eth")
    else:
        return await message.answer("Не знаю такої команди 🤔")

    await message.answer(f"Ціна {text.upper()}: *{price} USD*", parse_mode="Markdown")


# ===== Запуск =====
async def main():
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
