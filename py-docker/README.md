


### Estrutura de Diretório

```
.
├── app
│   ├── __init__.py
│   └── main.py
├── Dockerfile
└── requirements.txt
```

### Construindo a Imagem Docker

`docker build -t myimage .`

### Iniciando o contêiner Docker

`docker run -d --name mycontêiner -p 80:80 myimage`

### Documentação interativa da API que utiliza a FatsAPI

 Acesse http://192.168.99.100/docs ou http://127.0.0.1/docs (ou equivalente, usando seu host Docker).





### DICAS

1. Se você está executando seu contêiner atrás de um Proxy de Terminação TLS (load balancer) como Nginx ou Traefik, adicione a opção --proxy-headers, isso fará com que o Uvicorn confie nos cabeçalhos enviados por esse proxy, informando que o aplicativo está sendo executado atrás do HTTPS, etc.

`CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]`











### Instale o Python

```bash
apt-get install python3 python3-pip
```

### Instale o framework de desenvolvimento de APIRest: FASTAPI 

```bash
- pip3 install fastapi 
```

### Instale o servidor Web (Servidor ASGI) 

```bash
- pip3 install "uvicorn[standard]"
```

Como usar:
```bash
uvicorn api:app --reload
# “--reload”  é responsável toda vez que atualizar o projeto 
```
 
