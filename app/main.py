from fastapi import FastAPI  # Importa a biblioteca FastAPI para criar APIs

# Cria a aplicação FastAPI
app = FastAPI()

# Endpoint para verificar o estado do sistema

@app.get("/health")
def health_check():
    return {"status": "healthy"}  # Resposta da aplicação
