import os
import requests
import math
from dotenv import load_dotenv
from datetime import datetime

# Configurações iniciais
# Importar a chave da API do arquivo .env
load_dotenv()
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

# Verifique se a chave da API está definida
if not WEATHER_API_KEY:
    raise Exception("A chave da API do clima não está definida no arquivo .env")

# Salve a chave da API na variável key
key = WEATHER_API_KEY
locationKey = "2733005"

emojis = {
    1: "☀️",
    2: "☀️",
    3: "🌤",
    4: "🌤",
    5: "🌤",
    6: "🌥",
    7: "☁️",
    8: "☁️",
    11: "🌫",
    12: "🌧",
    13: "🌦",
    14: "🌦",
    15: "⛈",
    16: "⛈",
    17: "🌦",
    18: "🌧",
    19: "🌨",
    20: "🌨",
    21: "🌨",
    22: "❄️",
    23: "❄️",
    24: "🌧",
    25: "🌧",
    26: "🌧",
    29: "🌧",
    30: "🌫",
    31: "🥵",
    32: "🥶"
}

# Construir a URL da API
url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{locationKey}?apikey={key}"

# Fazer a requisição à API
response = requests.get(url)
data = response.json()

# Extrair dados relevantes da resposta
target = data['DailyForecasts'][0]
degF = target['Temperature']['Maximum']['Value']
degC = round((degF - 32) / 1.8)
icon = emojis.get(target['Day']['Icon'])

# Calcular o tempo desde 1 de julho de 2008
psTime = datetime.now().year - datetime(2023, 2, 15).year
todayDay = datetime.now().strftime("%A")

# Ler o template SVG
with open('./template.svg', 'r', encoding='utf-8') as file:
    svg_data = file.read()

# Substituir placeholders no template
svg_data = svg_data.replace("{degF}", str(degF))
svg_data = svg_data.replace("{degC}", str(degC))
svg_data = svg_data.replace("{weatherEmoji}", icon)
svg_data = svg_data.replace("{psTime}", str(psTime))
svg_data = svg_data.replace("{todayDay}", todayDay)

# Salvar o SVG atualizado
with open('./chat.svg', 'w', encoding='utf-8') as file:
    file.write(svg_data)
