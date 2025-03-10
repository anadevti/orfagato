﻿# Usando uma imagem base Python
FROM python:3.12

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o arquivo requirements.txt e instalando as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiando todo o código do projeto para dentro do container
COPY . /app/

# Expondo a porta que o Django usará
EXPOSE 8000

# Executando as migrações antes de iniciar o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]