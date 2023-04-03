import requests  # pip3 install requests
# OpenWeather API Key
API_KEY = "949d1u22cbffbrarjh182eig55"  # this API does not work. You need to get your own API key from OpenWeather
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("The weather is ", weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    print("temperature is ", temperature, " degrees celcius")
    print(data)
else:
    print(f"Error: {response.status_code}")
print("Part of the 5 mini projects from YouTube sensation -> Tech With Tim")
