


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

`docker build -t img-app .`

### Iniciando o contêiner Docker

`docker run -d --rm --name app -p 80:80 img-app`

- Para habilitar a execução do contêiner na inicialização e habilitar reinicializações em falhas<br>
`docker run -d --restart --name app -p 80:80 img-app`

### Documentação interativa da API que utiliza a FatsAPI

 Acesse http://127.0.0.1/docs (ou equivalente, usando seu host Docker).







