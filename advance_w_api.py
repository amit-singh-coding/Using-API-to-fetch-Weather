import requests
Api_Key='6cde83dd330b957babe2818528afb811'
def data_get():
    state=state_name.get()
    weather_data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+state+"&appid="+Api_Key+"").json()
    tamp_lable_1.config(text=str(int(weather_data["main"]["temp"]-273.15))+" ℃")
    tamp_lable_2.config(text=str(int(weather_data["main"]["temp"]-273.15)))
    tamp_F_lable_1.config(text=str(int(((weather_data["main"]["temp"]-273.15)*9/5)+32))+" ℉")
    wind_lable_1.config(text=str(int(weather_data["wind"]["speed"]*3600/1000))+' km/h')
    wD_lable_1.config(text=str(weather_data["weather"][0]["main"]))
    humidity_lable_1.config(text=str(weather_data["main"]["humidity"])+" %")
        
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("Project#1 Weather App Using API")
win.config(bg="Teal")
win.geometry("400x630")

name_lable=Label(win,text="Masai Weather App",font=("Arial",28,"bold"))
name_lable.place(x=14,y=25,height=40,width=370)
name_lable.config(bg="yellow")

indicate=Label(win,text="--:Select or type your state name :--",font=("Arial",15,"bold"))
indicate.place(x=14,y=77,height=30,width=370)
indicate.config(bg="MediumSpringGreen")

state_name=StringVar()
list_name=["Andhra Pradesh","Assam","Bihar","Chhattisgarh","Cherrapunji","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Mumbai","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman & Nicobar","Chandigarh","Dadra & Nagar Haveli","Daman & Diu","Lakshadweep","Delhi","Puducherry"]
com=ttk.Combobox(win,values=list_name,font=("Arial",18,"bold"),textvariable=state_name)
com.place(x=13,y=120,height=40,width=275)

wether_icon=Label(win,text="⛅",font=("Arial",150,))
wether_icon.place(x=-18,y=169,height=235,width=300)
wether_icon.config(bg="Teal")

tamp_lable=Label(win,text="🌞 Temperature",font=("Arial",15))
tamp_lable.place(x=14,y=370,height=40,width=200)
tamp_lable_1=Label(win,text="",font=("Arial",15,"bold"))
tamp_lable_1.place(x=235,y=370,height=40,width=149)

tamp_lable_2=Label(win,text="00",font=("Arial",80,"bold"))
tamp_lable_2.place(x=250,y=248,height=95,width=125)
tamp_lable_2.config(bg="Teal")
D_selsius_lable=Label(win,text="℃",font=("Arial",42,"bold"))
D_selsius_lable.place(x=330,y=202,height=52,width=55)
D_selsius_lable.config(bg="Teal")

tamp_F_lable=Label(win,text="☼ Temperature",font=("Arial",15))
tamp_F_lable.place(x=14,y=420,height=40,width=200)
tamp_F_lable_1=Label(win,text="",font=("Arial",15,"bold"))
tamp_F_lable_1.place(x=235,y=420,height=40,width=149)

wind_lable=Label(win,text="💨  Wind Speed",font=("Arial",15))
wind_lable.place(x=14,y=470,height=40,width=200)
wind_lable_1=Label(win,text="",font=("Arial",15,"bold"))
wind_lable_1.place(x=235,y=470,height=40,width=149)

wD_lable=Label(win,text="🌧  Description",font=("Arial",16))
wD_lable.place(x=14,y=520,height=40,width=200)
wD_lable_1=Label(win,text="",font=("Arial",15,"bold"))
wD_lable_1.place(x=235,y=520,height=40,width=149)

humidity_lable=Label(win,text="💧 Weather Humidity",font=("Arial",15))
humidity_lable.place(x=14,y=570,height=40,width=200)
humidity_lable_1=Label(win,text="",font=("Arial",15,"bold"))
humidity_lable_1.place(x=235,y=570,height=40,width=149)

search_button=Button(win,text="Search",font=("Arial",17,"bold"),command=data_get)
search_button.place(x=298,y=120,height=40,width=87)
search_button.config(bg="red")

win.mainloop()