from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Permite que o React converse com o Python sem bloqueios de segurança
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Estado inicial da conta simulada
conta_bancaria = {
    "saldo": 2500.00
}

class Transacao(BaseModel):
    valor: float

@app.get("/api/saldo")
def obter_saldo():
    return conta_bancaria

@app.post("/api/sacar")
def realizar_saque(transacao: Transacao):
    if transacao.valor <= 0:
        return {"erro": "O valor deve ser maior que zero."}
    if transacao.valor > conta_bancaria["saldo"]:
        return {"erro": "Saldo insuficiente para esta operação!"}
    
    conta_bancaria["saldo"] -= transacao.valor
    return {"mensagem": "Saque realizado com sucesso!", "saldo": conta_bancaria["saldo"]}

@app.post("/api/depositar")
def realizar_deposito(transacao: Transacao):
    if transacao.valor <= 0:
        return {"erro": "O valor deve ser maior que zero."}
        
    conta_bancaria["saldo"] += transacao.valor
    return {"mensagem": "Depósito realizado com sucesso!", "saldo": conta_bancaria["saldo"]}