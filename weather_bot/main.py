from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token="6373338069:AAH3RHcpUz-VsGRDRlTazAWguFCZumJvFQQ")
dp = Dispatcher(bot)
client = python_weather.Client(unit=python_weather.IMPERIAL)

@dp.message_handler()
async def echo(message:types.Message):
    if message.text == "/start":
        resp_msg = "Hello, my brother from another mother!" + "\n" + "Write the name of the place:"
    elif message.text == "/three_a":
        weather = await client.get("atyrau")
        celsius1 = (weather.current.temperature - 32) * (5 / 9)
        flcelsius1 = (weather.current.feels_like - 32) * (5 / 9)

        resp_msg = "\n" + str(weather.nearest_area.country) + ", " + str(weather.nearest_area.region) + "\n"
        resp_msg += "Temperature: " + str(round(celsius1)) + "°" + "\n"
        resp_msg += "Feels like: " + str(round(flcelsius1)) + "°" + "\n"
        resp_msg += "Wind speed: " + str(weather.current.wind_speed) + " MPH" + "\n"
        weather = await client.get("astana")
        celsius2 = (weather.current.temperature - 32) * (5 / 9)
        flcelsius2 = (weather.current.feels_like - 32) * (5 / 9)

        resp_msg += "\n" + "\n" + str(weather.nearest_area.country) + ", " + str(weather.nearest_area.region) + "\n"
        resp_msg += "Temperature: " + str(round(celsius2)) + "°" + "\n"
        resp_msg += "Feels like: " + str(round(flcelsius2)) + "°" + "\n"
        resp_msg += "Wind speed: " + str(weather.current.wind_speed) + " MPH" + "\n"
        weather = await client.get("almaty")
        celsius3 = (weather.current.temperature - 32) * (5 / 9)
        flcelsius3 = (weather.current.feels_like - 32) * (5 / 9)

        resp_msg += "\n" + "\n" + str(weather.nearest_area.country) + ", " + str(weather.nearest_area.region) + "\n"
        resp_msg += "Temperature: " + str(round(celsius3)) + "°" + "\n"
        resp_msg += "Feels like: " + str(round(flcelsius3)) + "°" + "\n"
        resp_msg += "Wind speed: " + str(weather.current.wind_speed) + " MPH"
    elif message.text == "/guw":
        weather = await client.get("atyrau")
        celsius1 = (weather.current.temperature - 32) * (5 / 9)
        flcelsius1 = (weather.current.feels_like - 32) * (5 / 9)

        resp_msg = "\n" + str(weather.nearest_area.country) + ", " + str(weather.nearest_area.region) + "\n"
        resp_msg += "Temperature: " + str(round(celsius1)) + "°" + "\n"
        resp_msg += "Feels like: " + str(round(flcelsius1)) + "°" + "\n"
        resp_msg += "Wind speed: " + str(weather.current.wind_speed) + " MPH" + "\n"
    elif message.text == "/nqz":
        weather = await client.get("astana")
        celsius1 = (weather.current.temperature - 32) * (5 / 9)
        flcelsius1 = (weather.current.feels_like - 32) * (5 / 9)

        resp_msg = "\n" + str(weather.nearest_area.country) + ", " + str(weather.nearest_area.region) + "\n"
        resp_msg += "Temperature: " + str(round(celsius1)) + "°" + "\n"
        resp_msg += "Feels like: " + str(round(flcelsius1)) + "°" + "\n"
        resp_msg += "Wind speed: " + str(weather.current.wind_speed) + " MPH" + "\n"
    elif message.text == "/ala":
        weather = await client.get("almaty")
        celsius1 = (weather.current.temperature - 32) * (5 / 9)
        flcelsius1 = (weather.current.feels_like - 32) * (5 / 9)

        resp_msg = "\n" + str(weather.nearest_area.country) + ", " + str(weather.nearest_area.region) + "\n"
        resp_msg += "Temperature: " + str(round(celsius1)) + "°" + "\n"
        resp_msg += "Feels like: " + str(round(flcelsius1)) + "°" + "\n"
        resp_msg += "Wind speed: " + str(weather.current.wind_speed) + " MPH" + "\n"
    else:
        weather = await client.get(message.text)
        celsius = (weather.current.temperature - 32) * (5 / 9)
        flcelsius = (weather.current.feels_like - 32) * (5 / 9)

        resp_msg = str(weather.nearest_area.country) + ", " + str(weather.nearest_area.region) + "\n"
        resp_msg += "Temperature: " + str(round(celsius)) + "°" + "\n"
        resp_msg += "Feels like: " + str(round(flcelsius)) + "°" + "\n"
        resp_msg += "Wind speed: " + str(weather.current.wind_speed) + " MPH"

    await message.answer(resp_msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
