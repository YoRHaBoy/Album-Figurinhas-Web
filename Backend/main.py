import os
import glob
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Inicializa a aplicação FastAPI
app = FastAPI()

# Configuração do Middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definindo os caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "Imagens")

# Lista com as 30 figurinhas do álbum.
# Apenas as figurinhas cujas imagens existem na pasta (IDs 1 a 5) estão ativas.
# As figurinhas restantes (IDs 6 a 30) estão comentadas até que as imagens fiquem disponíveis.
figurinhas = [
    {
        "id": 1,
        "nome": "Cloud Strife",
        "categoria": "Protagonistas",
        "imagem_url": "/figurinhas/1/imagem"
    },
    {
        "id": 2,
        "nome": "Squall Leonheart",
        "categoria": "Protagonistas",
        "imagem_url": "/figurinhas/2/imagem"
    },
    {
        "id": 3,
        "nome": "Zidane Tribal",
        "categoria": "Protagonistas",
        "imagem_url": "/figurinhas/3/imagem"
    },
    {
        "id": 4,
        "nome": "Tidus",
        "categoria": "Protagonistas",
        "imagem_url": "/figurinhas/4/imagem"
    },
    {
        "id": 5,
        "nome": "Noctis Lucis Caelum",
        "categoria": "Protagonistas",
        "imagem_url": "/figurinhas/5/imagem"
    },
    # {
    #     "id": 6,
    #     "nome": "Aerith Gainsborough",
    #     "categoria": "Heroínas",
    #     "imagem_url": "/figurinhas/6/imagem"
    # },
    # {
    #     "id": 7,
    #     "nome": "Tifa Lockhart",
    #     "categoria": "Heroínas",
    #     "imagem_url": "/figurinhas/7/imagem"
    # },
    # {
    #     "id": 8,
    #     "nome": "Yuna",
    #     "categoria": "Heroínas",
    #     "imagem_url": "/figurinhas/8/imagem"
    # },
    # {
    #     "id": 9,
    #     "nome": "Lightning",
    #     "categoria": "Heroínas",
    #     "imagem_url": "/figurinhas/9/imagem"
    # },
    # {
    #     "id": 10,
    #     "nome": "Terra Branford",
    #     "categoria": "Heroínas",
    #     "imagem_url": "/figurinhas/10/imagem"
    # },
    # {
    #     "id": 11,
    #     "nome": "Sephiroth",
    #     "categoria": "Vilões",
    #     "imagem_url": "/figurinhas/11/imagem"
    # },
    # {
    #     "id": 12,
    #     "nome": "Kefka Palazzo",
    #     "categoria": "Vilões",
    #     "imagem_url": "/figurinhas/12/imagem"
    # },
    # {
    #     "id": 13,
    #     "nome": "Kuja",
    #     "categoria": "Vilões",
    #     "imagem_url": "/figurinhas/13/imagem"
    # },
    # {
    #     "id": 14,
    #     "nome": "Ardyn Izunia",
    #     "categoria": "Vilões",
    #     "imagem_url": "/figurinhas/14/imagem"
    # },
    # {
    #     "id": 15,
    #     "nome": "Seymour Guado",
    #     "categoria": "Vilões",
    #     "imagem_url": "/figurinhas/15/imagem"
    # },
    # {
    #     "id": 16,
    #     "nome": "Bahamut",
    #     "categoria": "Summons",
    #     "imagem_url": "/figurinhas/16/imagem"
    # },
    # {
    #     "id": 17,
    #     "nome": "Shiva",
    #     "categoria": "Summons",
    #     "imagem_url": "/figurinhas/17/imagem"
    # },
    # {
    #     "id": 18,
    #     "nome": "Ifrit",
    #     "categoria": "Summons",
    #     "imagem_url": "/figurinhas/18/imagem"
    # },
    # {
    #     "id": 19,
    #     "nome": "Odin",
    #     "categoria": "Summons",
    #     "imagem_url": "/figurinhas/19/imagem"
    # },
    # {
    #     "id": 20,
    #     "nome": "Ramuh",
    #     "categoria": "Summons",
    #     "imagem_url": "/figurinhas/20/imagem"
    # },
    # {
    #     "id": 21,
    #     "nome": "Guerreiro (Warrior)",
    #     "categoria": "Jobs",
    #     "imagem_url": "/figurinhas/21/imagem"
    # },
    # {
    #     "id": 22,
    #     "nome": "Mago Negro (Black Mage)",
    #     "categoria": "Jobs",
    #     "imagem_url": "/figurinhas/22/imagem"
    # },
    # {
    #     "id": 23,
    #     "nome": "Mago Branco (White Mage)",
    #     "categoria": "Jobs",
    #     "imagem_url": "/figurinhas/23/imagem"
    # },
    # {
    #     "id": 24,
    #     "nome": "Dragoneiro (Dragoon)",
    #     "categoria": "Jobs",
    #     "imagem_url": "/figurinhas/24/imagem"
    # },
    # {
    #     "id": 25,
    #     "nome": "Ladrão (Thief)",
    #     "categoria": "Jobs",
    #     "imagem_url": "/figurinhas/25/imagem"
    # },
    # {
    #     "id": 26,
    #     "nome": "Chocobo",
    #     "categoria": "Mascotes",
    #     "imagem_url": "/figurinhas/26/imagem"
    # },
    # {
    #     "id": 27,
    #     "nome": "Moogle",
    #     "categoria": "Mascotes",
    #     "imagem_url": "/figurinhas/27/imagem"
    # },
    # {
    #     "id": 28,
    #     "nome": "Tonberry",
    #     "categoria": "Mascotes",
    #     "imagem_url": "/figurinhas/28/imagem"
    # },
    # {
    #     "id": 29,
    #     "nome": "Cactuar",
    #     "categoria": "Mascotes",
    #     "imagem_url": "/figurinhas/29/imagem"
    # },
    # {
    #     "id": 30,
    #     "nome": "Guerreiro da Luz (Você)",
    #     "categoria": "Lendas",
    #     "imagem_url": "/figurinhas/30/imagem"
    # }
]

# Endpoint GET "/figurinhas" - Retorna a lista de figurinhas ativas
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# Endpoint GET "/figurinhas/{id}/imagem" - Busca e retorna a imagem correspondente ao ID
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)

    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    return FileResponse(arquivos[0])
