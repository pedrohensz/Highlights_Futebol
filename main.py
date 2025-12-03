from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

key = "MjU4NzE0XzE3NjQ3NjY4NTFfZjYyNzQxZGFjYWU2YzQ2ZTFiNjIzNTY5NDgyMzFjYzJjOWU2YmUzOQ=="
url = f"https://www.scorebat.com/video-api/v3/free-feed/?token={key}"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],)

@app.get("/Gols")
def ver_gols():
    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        return dados_json
    else:
        print(f"O erro foi {response.status_code}")

url_agendamento = "https://api.football-data.org/v4/matches"
token_schedule = "bf2f015dd3a1400496c3a5858da858f0"
@app.get("/Schedule")
def partidas():
    headers = {
    "X-Auth-Token": token_schedule 
    }
    response_agendamento = requests.get(url_agendamento, headers=headers)
    if response_agendamento.status_code == 200:
        dados_json = response_agendamento.json()
        return dados_json
    else:
        print(f"O erro foi {response_agendamento.status_code}")

    