from aiogram import Bot, Dispatcher, executor, types
import python_weather
import asyncio
import os

#bot init
bot = Bot(token="5778697521:AAE3tj-0vUcHpsb0s1sT1Pu3FUZZ-DOoVlI")
dp = Dispatcher(bot)

async def getweather():
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:

#echo
@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)
    celsius = (weather.current.temperature - 32) * 5 / 9
    resp_msg = f"Temperature:  + {celsius}"

    await message.answer(message.text)



#run-longpolling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

