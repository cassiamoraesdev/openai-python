# Use uma imagem base do Python
FROM python:3.8-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os requisitos do projeto para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o script Python para o contêiner
COPY seu_script.py .

# Configure a chave da API como uma variável de ambiente
ENV OPENAI_API_KEY="SUA_CHAVE_DA_API_OPENAI"

# Comando para executar o script Python quando o contêiner for iniciado
CMD ["python", "seu_script.py"]
