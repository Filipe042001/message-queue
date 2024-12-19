from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criar a conexão com o SQLite
DATABASE_URL = "sqlite:///./messages.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos do SQLAlchemy
Base = declarative_base()

# Modelo da tabela de mensagens
class MessageModel(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, index=True)  # ID único
    message = Column(Text, nullable=False)  # Conteúdo da mensagem
