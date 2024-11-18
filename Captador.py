import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

# Função que busca a temperatura e umidade da API e salva em um arquivo txt
def fetch_and_save_weather_data():
    try:
        # Endpoint da API com cidade e chave (substitua pela chave da API)
        api_key = "d1a0eb1c3042af1490db344238b57efa"
        city = "São Paulo"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        # Chamada da API
        response = requests.get(url)
        data = response.json()
        
        # Extração da temperatura e umidade
        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Formatação dos dados
            line = f"Data/Hora: {timestamp} | Cidade: {city} | Temperatura: {temperature}°C | Umidade: {humidity}%\n"
            
            # Salvando no arquivo txt
            with open("temperatura.txt", "a") as file:
                file.write(line)
            
            messagebox.showinfo("Sucesso", f"Temperatura de {temperature}°C e umidade de {humidity}% registradas com sucesso!")
        else:
            messagebox.showerror("Erro", f"Erro ao buscar dados: {data['message']}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Interface Gráfica
app = tk.Tk()
app.title("Clima")
app.geometry("300x200")

button = tk.Button(app, text="Buscar Dados do Clima", command=fetch_and_save_weather_data)
button.pack(pady=50)

app.mainloop()
