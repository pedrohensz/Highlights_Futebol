from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
import os 
app = FastAPI()

key = str(os.environ.get('key'))

url = f"https://www.scorebat.com/video-api/v3/free-feed/?token={key}"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/Gols")
def ver_gols():
    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        return dados_json
    else:
        print(f"O erro foi {response.status_code}")

url_agendamento = "https://api.football-data.org/v4/competitions"
token_schedule = "bf2f015dd3a1400496c3a5858da858f0"
@app.get("/Partidas")
def partidas():
    headers = {"X-Auth-Token": token_schedule}
    response = requests.get(url_agendamento, headers=headers)

    if response.status_code == 200:
        dados = response.json()
        return {"response": dados}  
        # agora seu front consegue usar partidas.response
    else:
        return {"erro": response.status_code}