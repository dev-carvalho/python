


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







