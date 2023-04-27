


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

`docker build -t img-py-app .`

### Iniciando o contêiner Docker

`docker run -d --name py-app -p 80:80 img-py-app`

- Para habilitar a execução do contêiner na inicialização e habilitar reinicializações em falhas
`docker run -d --restart --name py-app -p 80:80 img-py-app`

### Documentação interativa da API que utiliza a FatsAPI

 Acesse http://127.0.0.1/docs (ou equivalente, usando seu host Docker).







