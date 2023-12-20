import python_weather

import asyncio
import os


async def getweather():

    async with python_weather.Client(unit=python_weather.IMPERIAL ) as client:

        weather = await client.get('Atyrau')

        celsius = (weather.current.temperature - 32) * (5/9)
        print("Temperature: " + str(round(celsius)) + "°")

        flcelsius = (weather.current.feels_like - 32) * (5/9)
        print("Feels like: " + str(round(flcelsius)) + "°")

        print("Wind speed: " + str(weather.current.wind_speed) + " MPH")

        print("Location: " + str(weather.nearest_area.country) + ", " + str(weather.nearest_area.region ))

        for forecast in weather.forecasts:
            print(forecast)

            for hourly in forecast.hourly:
                print(f' --> {hourly!r}')


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())