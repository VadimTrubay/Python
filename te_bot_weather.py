import python_weather
import asyncio
import os

async def getweather():
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        weather = await client.get("Odessa")
        celsius = (weather.current.temperature - 32) * 5/9
        print("Temperature: " + str(round(celsius, 1)) + "°")
        print("Sky: " + str(weather.current.type.Sunny))
        print("Wind: " + str(weather.current.wind_speed) + " m/sec")
        print()

        # get the weather forecast for a few days
        #for forecast in weather.forecasts:
            #print(forecast.date, forecast.astronomy)

            # hourly forecasts
            #for hourly in forecast.hourly:
                #print(f' --> {hourly!r}')


if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(getweather())