
from tkinter import *
from tkinter import ttk
import requests
def data_get():
 city=city_name.get()
 data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cf5a97c5ce5f315e4a50ab9e7c4cc7de").json()
 w_label1.config(text=data["weather"][0]["main"])
 d_label1.config(text=data["weather"][0]["description"])



 temp_label1.config(text=str(data["main"]["temp"]-273.15))
 pressure_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather Predictor")
win.config(bg="blue")
win.geometry("500x540")
name_label = Label(win,text="WEATHER PREDICTOR",font=("Time New Roman",20,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()
list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="WEATHER PREDICTOR",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label = Label(win,text="WEATHER ",font=("Time New Roman",10,"bold"))
w_label.place(x=25,y=260,height=50,width=150)
w_label1 = Label(win,text=" ",font=("Time New Roman",10,"bold"))
w_label1.place(x=250,y=260,height=50,width=150)
d_label = Label(win,text="DESCRIPTION",font=("Time New Roman",10,"bold"))
d_label.place(x=25,y=330,height=50,width=150)
d_label1 = Label(win,text="",font=("Time New Roman",10,"bold"))
d_label1.place(x=250,y=330,height=50,width=150)

temp_label = Label(win,text="TEMPERATURE",font=("Time New Roman",10,"bold"))
temp_label.place(x=25,y=400,height=50,width=150)

temp_label1 = Label(win,text=" ",font=("Time New Roman",10,"bold"))
temp_label1.place(x=250,y=400,height=50,width=150)


pressure_label = Label(win,text="PRESSURE",font=("Time New Roman",10,"bold"))
pressure_label.place(x=25,y=470,height=50,width=150)

pressure_label1 = Label(win,text=" ",font=("Time New Roman",10,"bold"))
pressure_label1.place(x=250,y=470,height=50,width=150)



done_button= Button(win,text="Done",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)




win.mainloop()
