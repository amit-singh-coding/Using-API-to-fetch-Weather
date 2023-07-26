import requests
Api_key="6cde83dd330b957babe2818528afb811"
user_input=input("Enter your city or state name here-> ")
data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+user_input+"&appid="+Api_key+"").json()
#print(data)
temperature=str(int(data["main"]["temp"]-273.15))+" ℃"
windspeed=str(int(data["wind"]["speed"]*3600/1000))+' km/h'
w_humidity=str(data["main"]["humidity"])+" %"
print('''
<<-------------Weather Data of '''+user_input+'''------------>>
      ''')
print("Temperature -> "+temperature)
print("Windspeed -> "+windspeed)
print("Humidity -> "+w_humidity)
print()
