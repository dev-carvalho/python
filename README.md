

- Instalação do Python
apt-get install python3 python3-pip

- Alias
alias python=python3


### Framework de desenvolvimento

- Biblioteca da API: FastAPI

pip3 install fastapi 
pip install -U http-exceptions  

- Servidor Web (Servidor ASGI) aplicação

pip3 install "uvicorn[standard]"






### Para rodar a  API (api.py)

uvicorn api:app --reload

- “ — reload”, que é responsável por atualizar o projeto toda vez que o arquivo api.py é modificado
 