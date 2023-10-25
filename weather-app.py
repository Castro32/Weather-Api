import requests
import tkinter as tk
from tkinter import messagebox
def get_weather():
    city = city_entry.get()
    api_key = 'cabe4b4c8e2078bf63d1d5fabe9bd6da'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        
        if data['cod'] != '404':
           try:
               temperature = data['main']['temp']   
               description = data['weather'][0]['description']
               messagebox.showinfo("Weather Information", f"Temperature: {temperature}°C\nDescription: {description}")
           except KeyError:
               messagebox.showerror("Error", "Failed to retrieve temperature data.") 
        else:
            messagebox.showerror("Error", "City Not Found") 
    except requests.exceptions.RequestException:    
            messagebox.showerror("Error", "Failed to connect to the weather service.")
           


window = tk.Tk()
window.title('WeatherApp')
window.geometry("600x500")
window.resizable(True, True)

city_label =tk.Label(window, text ="City:")
city_label.pack()

city_entry =tk.Entry(window)
city_entry.pack()

get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.pack()

window.mainloop()
            
