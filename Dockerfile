# Usar uma imagem base com Python
FROM python:3.11-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os requisitos do projeto para o container
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o container
COPY ./app ./app

# Expor a porta em que o servidor vai rodar (8000)
EXPOSE 8000

# Definir o comando para executar o servidor com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
