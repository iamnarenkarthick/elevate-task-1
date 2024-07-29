import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Function to get weather data from OpenWeatherMap API
def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to display weather data
def display_weather():
    location = entry.get()
    if not location:
        messagebox.showerror("Error", "Please enter a city name or ZIP code")
        return
    
    weather_data = get_weather(api_key, location)
    if weather_data:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        
        result_text.set(f"Weather in {city}:\n"
                        f"Temperature: {temperature}°C\n"
                        f"Humidity: {humidity}%\n"
                        f"Description: {description.capitalize()}")
    else:
        messagebox.showerror("Error", "Unable to fetch weather data. Please check the city name or ZIP code and try again.")

# OpenWeatherMap API key
api_key = "fed0dc178cf8b0ea7304cb68fe662322"

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Set the window size
root.geometry("400x300")

# Style configuration
style = ttk.Style()
style.configure('TFrame', background='#FFFFFF')  # White background
style.configure('TLabel', background='#FFFFFF', foreground='#000000', font=('Times New Roman', 12))  # Black text
style.configure('TButton', background='#FFFFFF', foreground='#000000', font=('Times New Roman', 12))  # Black text
style.configure('TEntry', background='#FFFFFF', foreground='#000000', font=('Times New Roman', 12))  # Black text

# Create and place the widgets
frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame')
frame.pack(fill=tk.BOTH, expand=True)

label = ttk.Label(frame, text="Enter city name or ZIP code:", style='TLabel')
label.grid(row=0, column=0, padx=5, pady=5)

entry = ttk.Entry(frame, width=30, style='TEntry')
entry.grid(row=0, column=1, padx=5, pady=5)

button = ttk.Button(frame, text="Get Weather", command=display_weather, style='TButton')
button.grid(row=0, column=2, padx=5, pady=5)

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, justify="left", style='TLabel')
result_label.pack(pady=20, padx=20)

# Start the Tkinter event loop
root.mainloop()
