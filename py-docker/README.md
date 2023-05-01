## Descrição do Projeto
Construção do ecosistema de um Micro-serviço contruido em Python utilizando:
- bbiblioteca FastAPI (Padrão REST);
- Banco de Dados PostGreSQL e sua Administração (pgadmin);

<br>

### Estrutura de Diretório

```
.
├── app
│   ├── __init__.py
│   └── main.py
├── Dockerfile
└── requirements.txt
```

<br>

## Construindo a Imagem da Aplicação via Dockerfile

`docker build -t img-app .`

### Iniciando o contêiner Docker

`docker run -d --rm --name app -p 80:80 img-app`

- Para habilitar a execução do contêiner na inicialização e habilitar reinicializações em falhas<br>
`docker run -d --restart on-failure --name app -p 80:80 img-app`

<br>

## Construindo da Infra-estrutura necessária para a Aplicação

- UP/Levanta a infra-estrutura: <br>
`docker-compose up -d`

- DOWN/Derubar a infra-estrutura da Aplicação: <br>
`docker-compose down`

<br>

## Micro-Serviço via FastAPI do Phython 

### Documentação interativa da API que utiliza a FatsAPI

 Acesse http://127.0.0.1/docs (ou equivalente, usando seu host Docker).

<br>



