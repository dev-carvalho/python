
## API REST para executar operações CRUD usando FastAPI com MySQL

### Instale as Dependências
- Instale FastAPI: `pip install fastapi`
- Instale uvicorn: `pip install uvicorn`
- Instale PyMySQL: `pip install PyMySQL`
- Instale o SQLAlchemy: `pip install SQLAlchemy`
- Instale o pydantic para validar o e-mail: `pip install pydantic[email]`

#### O que são 
- Uvicorn é uma implementação do servidor ASGI para desempenho rápido.
- PyMySQL é uma biblioteca cliente Python MySQL pura.
- SQLAlchemy é um Python SQL Object Relational Mapper que fornece capacidade e flexibilidade completas de SQL para desenvolvedores de aplicativos. Ele fornece uma coleção de padrões de persistência de nível empresarial bem conhecidos para acesso rápido e de alto desempenho ao banco de dados.

### Criar banco de dados e tabelas

- Crie o banco de dados my_test_db usando o seguinte script MySQL:
`CREATE DATABASE my_test_db;`

- Crie uma tabela de produtos usando o seguinte script MySQL:

``` 
USE my_test_db;
CREATE TABLE IF NOT EXISTS product(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(1024),
    price BIGINT DEFAULT 0,
    is_available BOOLEAN DEFAULT FALSE,
    seller_email VARCHAR(512),
    deleted BOOLEAN DEFAULT FALSE,
    created_by INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT NULL,
    updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE = INNODB;
```