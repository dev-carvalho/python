# Autor: Marcos Antonio de Carvalho
# Descrição: Construção em vários estágios de container Docker
#            para aplicações em linguagem Python.

# Inspiração:
#  - https://testdriven.io/blog/docker-best-practices/
#  - https://fastapi.tiangolo.com/pt/deployment/docker/

# Use um estágio para compilar e construir seu aplicativo. Como apenas
# o estágio final é usado para criar a imagem, as dependências e ferramentas
# associadas à construção de seu aplicativo são descartadas, deixando uma 
# imagem enxuta e modular pronta para produção.

##---------------------------##
##      FASE TEMPORARIA      ##
##  COMPILAÇÃO E CONSTRUÇÃO  ##
##---------------------------##

# temp stage (Fase Temporaria)
FROM python:3.11.1-slim as builder

# Diretório da aplicação
WORKDIR /code

# Configura Variáveis de Ambiente
# -------------------------------
# PYTHONDONTWRITEBYTECODE: Impede que o Python grave arquivos pyc no disco 
# (equivalente à opção python -B)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Impede que o Python armazene em buffer stdout e stderr 
# (equivalente a opção python -u)
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Lista dos requisitos minimos
COPY ./requirements.txt /code/requirements.txt

# Instala os requisitos minimos
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /code/wheels -r /code/requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


##--------------##
##  FASE FINAL  ##
##--------------##

# final stage (Fase Final)
FROM python:3.11.1-slim 

# Diretório da aplicação
WORKDIR /code

COPY --from=builder /code/wheels /wheels
COPY --from=builder /code/requirements.txt .

RUN pip install --no-cache /wheels/*

# Código do projeto da aplicação
COPY ./app /code/app

# Inicia o WebServer e a apliacação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# Se você está executando seu contêiner atrás de um Proxy de Terminação TLS (load balancer) 
# como Nginx ou Traefik, adicione a opção --proxy-headers, isso fará com que o Uvicorn confie 
# nos cabeçalhos enviados por esse proxy, informando que o aplicativo está sendo executado
#  atrás do HTTPS, etc.
# CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

# RESUMO:
#  compilações de vários estágios podem diminuir o tamanho de suas imagens de produção,
#  ajudando você a economizar tempo e dinheiro. Além disso, isso simplificará seus 
#  contêineres de produção. Além disso, devido ao tamanho menor e à simplicidade, 
#  há uma superfície de ataque potencialmente menor.

##
# End.




##-----------##
##  BUILDER  ##
##-----------##
#
# docker build -t py-app .
# docker build -t py-app-crud-api-rest-postgres .
#
# docker run --name app -it py-app-crud-api-rest-postgres
#
# docker run --name app -d py-app
#



# docker container start app
#  docker container exec -it app  /bin/sh