import requests
import json
import pyttsx3
city=input("Enter the name of the city\n")
url=f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r=requests.get(url)
# print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
print(w)
engine = pyttsx3.init()
engine.say(f"The current weather in {city} is {w}")
engine.runAndWait()