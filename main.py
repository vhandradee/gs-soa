from fastapi import FastAPI
from services.blackout_service import get_blackout_response
from models.database import create_db_and_table

app = FastAPI(
    title="GS-SOA",
    description="Sistema de Resposta a Quedas de Energia - simula a identificação de bairros afetados por apagões.",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    create_db_and_table()

@app.get("/", summary="Teste da API", description="Retorna uma mensagem padrão confirmando que a API está no ar.")
def home():
    return {"mensagem": "API GS-SOA funcionando"}

@app.get("/blackout/{bairro}", summary="Verificar queda", description="Verifica se há uma queda de energia no bairro informado.")
def verificar_blackout(bairro: str):
    return get_blackout_response(bairro)
