import requests
import threading
import tkinter as tk 
from tkinter import ttk


key = '9d5f8152dcab4047b6864935242812'


def check_weather():
    listbox.delete(0, tk.END)
    city = city_entry.get()
    if not city or city == 'Auto':
        city = 'auto:ip'
    weather = requests.get(f'http://api.weatherapi.com/v1/current.json?key={key}&q={city}')
    if weather.status_code == 200:
        listbox.insert(tk.END, weather.json()['location']['name'])
        listbox.insert(tk.END, 'Time: ' + str(weather.json()['location']['localtime']))
        listbox.insert(tk.END, 'Temp: ' + str(weather.json()['current']['temp_c']) + '(C)')
        listbox.insert(tk.END, 'Temp feels like: ' + str(weather.json()['current']['feelslike_c']) + '(C)')
        listbox.insert(tk.END, 'Weather: ' + str(weather.json()['current']['condition']['text']))
        listbox.insert(tk.END, 'Wind speed: ' + str(weather.json()['current']['wind_kph']) + '(kph)')
        listbox.insert(tk.END, 'Wind direction: ' + str(weather.json()['current']['wind_dir']))
        listbox.insert(tk.END, 'Lenth visible: ' + str(weather.json()['current']['vis_km']) + '(km)')
    else:
        listbox.insert(tk.END, 'Error')


window = tk.Tk()
window.title('Weather App')
window.geometry('300x300')
window.resizable(True, True)

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text='City name(Latitude and Longitude, Auto):')
city_entry = ttk.Entry(frame, width=30)
city_entry.grid(row=0, column=1)
city_entry.insert(0, 'Auto')

btn_start = ttk.Button(frame, text="Check weather", command=check_weather)
btn_start.grid(row=0, column=2, pady=10)

listbox = tk.Listbox(window, width=50, height=15)
listbox.grid(row=1, column=0, sticky=(tk.W, tk.E))


window.mainloop()


stop_event = threading.Event()
# x = requests.get(f'https://api.weatherapi.com/v1/current.json?key={key}&q={city}')

# print(x.json()['location']['name'])
# print('Time: ' + str(x.json()['location']['localtime']))
# print('Temp: ' + str(x.json()['current']['temp_c']) + '(C)')
# print('Temp feels like: ' + str(x.json()['current']['feelslike_c']) + '(C)')
# print('Condition: ' + str(x.json()['current']['condition']['text']))
# print('Wind speed: ' + str(x.json()['current']['wind_kph']) + '(kph)')
# print('Wind direcion: ' + str(x.json()['current']['wind_dir']))
# print('Length visible: ' + str(x.json()['current']['vis_km']) + '(km)')