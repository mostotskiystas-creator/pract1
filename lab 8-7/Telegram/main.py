import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8096671270:AAE9sgF1Ia3vEiSCqWy4x48pIBsYF9YEwJs"

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def get_price(symbol):
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


@dp.message(Command("start"))
async def start(message: types.Message):

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💎 TON")],
            [KeyboardButton(text="₿ BTC")],
            [KeyboardButton(text="Ξ ETH")],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

    await message.answer("Вибери криптовалюту:", reply_markup=keyboard)


@dp.message()
async def handle_buttons(message: types.Message):

    t = message.text.strip().lower()

    # Перевірки по emoji:
    if "ton" in t or "💎" in t:
        price = await get_price("ton")
        coin = "TON"

    elif "btc" in t or "₿" in t:
        price = await get_price("btc")
        coin = "BTC"

    elif "eth" in t or "ξ" in t:   # <— ДОДАНО: тут ловим ETH
        price = await get_price("eth")
        coin = "ETH"

    else:
        return await message.answer("Не знаю такої команди 🤔")

    await message.answer(f"💰 Ціна {coin}: *{price} USD*", parse_mode="Markdown")


async def main():
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
