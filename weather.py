from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d4e9258df1c69aa9b0e6f8cb177f9a6a").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label2.config(text=data["weather"][0]["description"])
    temp_label3.config(text=str(int(data["main"]["temp"]-273.15)))
    press_label4.config(text=data["main"]["pressure"])
win = Tk()
win.title("Wscube Tech")
win.config(bg = "skyblue") 
win.geometry("500x500")

name_label = Label(win,text="Weather App",font =("Time New Roman",40,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win ,text="Weather App" ,values=list_name ,font =("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=75,y=120,height=50,width=350)

w_label = Label(win,text="Weather Climate",font =("Time New Roman",10))
w_label.place(x=70,y=260,height=50,width=100)
w_label1 = Label(win,text="",font =("Time New Roman",10))
w_label1.place(x=210,y=260,height=50,width=100)

wd_label = Label(win,text="Weather Description",font =("Time New Roman",8))
wd_label.place(x=70,y=320,height=50,width=100)
wd_label2 = Label(win,text="",font =("Time New Roman",8))
wd_label2.place(x=210,y=320,height=50,width=100)

temp_label = Label(win,text="Weather Temp",font =("Time New Roman",10))
temp_label.place(x=70,y=380,height=50,width=100)
temp_label3 = Label(win,text="",font =("Time New Roman",8))
temp_label3.place(x=210,y=380,height=50,width=100)

press_label = Label(win,text="Weather pressure",font =("Time New Roman",9))
press_label.place(x=70,y=440,height=50,width=100)
press_label4 = Label(win,text="",font =("Time New Roman",10))
press_label4.place(x=210,y=440,height=50,width=100)

done_button = Button(win ,text="Done" ,font =("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()