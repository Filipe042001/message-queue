from fastapi import FastAPI  # Importa a biblioteca FastAPI para criar APIs


from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import uuid

from .database import Base, engine, SessionLocal, MessageModel

# Cria a aplicação FastAPI
app = FastAPI()

# Endpoint para verificar o estado do sistema

@app.get("/health")
def health_check():
    return {"status": "healthy"}  # Resposta da aplicação


# Inicializa as tabelas no SQLite
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão da base de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo de dados para FastAPI
class Message(BaseModel):
    message: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/messages")
def create_message(data: Message, db: Session = Depends(get_db)):
    message_id = str(uuid.uuid4())
    new_message = MessageModel(id=message_id, message=data.message)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return {"id": new_message.id, "status": "Message received"}

@app.get("/messages/{message_id}")
def get_message(message_id: str, db: Session = Depends(get_db)):
    message = db.query(MessageModel).filter(MessageModel.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"id": message.id, "message": message.message}
