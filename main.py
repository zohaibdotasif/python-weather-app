import requests
import os
import json

# URL: https://api.weatherapi.com/v1/current.json?key=7adf9cdf77504f41b2c52912230706&q=Paris

# API_KEY: 7adf9cdf77504f41b2c52912230706


def get_temperature(c):
    # url = f"https://api.weatherapi.com/v1/current.json?key=7adf9cdf77504f41b2c52912230706&q={city}"

    url = f"https://api.weatherapi.com/v1/forecast.json?key=7adf9cdf77504f41b2c52912230706&q={city}&days=2"

    resp = requests.get(url)
    if resp.status_code != 200:
        return "Oops! Something went wrong..."
    print(resp.text)
    weather_dict = json.loads(resp.text)
    temperature = weather_dict["current"]["temp_c"]
    return f"The temperature in {c} is {temperature} celsius"


os.system("echo 'Welcome! I am Weather App 1.0, created by Zohaib Asif.' | espeak")
print("Welcome! I am Weather App 1.0, created by Zohaib Asif.")
print("Press \\q to exit.")
os.system("echo 'Please enter the name of city: ' | espeak")
while True:
    city = input("Please enter the name of city: ")
    if city == "\q":
        os.system("echo 'Exiting weather app. Good Bye!' | espeak")
        break
    message = get_temperature(city)
    print(message)
    os.system(f"echo '{message}' | espeak")

