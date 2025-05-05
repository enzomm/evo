# Evo API (backend)

API desenvolvida em Python usando o framework FastAPI.

## Setup

Caso seu OS for Windows, recomenda-se para o ambiente usar o WSL em instância Debian.

### Docker/Docker-Compose

Para rodar o projeto usando docker siga os passos abaixo:

- Com o docker-compose é possível subir a imagem da API e o banco POSTGRES;
- Será necessário um arquivo .env na raíz do projeto com as variáveis de ambiente;
- Com o docker e docker-compose instalado na sua máquina e o arquivo .env configurado na pasta do projeto basta rodar o seguinte comando no seu terminal:

```bash
    # Você deve estar no diretório do projeto onde está o arquivo docker-compose.yml

    # Na primeira vez use a flag --build para construir as imagens
    $ docker-compose up -d --build
```

- **NOTA** -> Caso ocorra algum erro de incompatibilidade na versão do docker-compose, instale a mais recente:
```bash
    $ curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
- **NOTA** -> Caso ocorra algum erro do arquivo entrypoint.sh não ter permissão de execução, conceda:
```bash
    chmod +x entrypoint.sh
```

- Para verificar se tudo está como esperado use o comando:

```bash
    # Lista os containers ativos na sua máquina, você deverá ver o container da api e do db
    $ docker-compose ps
```

- Se tudo funcionou corretamente você pode acessar a documentação da api pelo seu browser no endereço **<http://127.0.0.1:8000/api/docs>**

### Local

Essa opção instala as dependências em um ambiente virtual direto na sua máquina.

- Você pode usar seu gerenciador de dependências python favorito, aqui vamos usar o **poetry**;
- Certifique-se de criar um ambiente virtual antes, abaixo um comando de exemplo:

```bash
    # Cria um diretório .venv com a versão do python ativa na sua máquina
    $ python -m venv .venv
```

- Para ativar o ambinte virtual com poetry use:

```bash
    poetry shell
```

- Para instalar as dependências rode:

```bash
    # Certifique-se de estar com o ambiente virtual ativo
    $ poetry install
```

- Com tudo instalado vamos rodar o projeto:

```bash
    poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

- Se tudo funcionou corretamente você pode acessar a documentação da api pelo seu browser no endereço **<http://127.0.0.1:8000/api/docs>**

- **NOTA** -> Perceba que nessa opção fica por sua responsabilidade instalar o banco postgres ou subir um container com ele e atualizar o arquivo **.env** com as configurações corretas.

### Criando as tabelas

Para aplicar as migrações (criar as tabelas baseado nos modelos) vamos usar o **alembic**.

- O arquivo de init e setup do alembic já esta pronto assim como as migrations necessárias devem estar atualizadas no repositório no diretório de migrations!
- Nesse cenário basta executar o respectivo comando:

```bash
    # Docker
    $ docker-compose run api alembic upgrade head
    # Poetry
    $ poetry run alembic upgrade head
```
# Evo App (frontend)

App desenvolvido em Vue.js 3 usando o framework Vite.

## Setup

Instale o **node.js** na sua máquina e tendo o arquivo **.env** (variáveis de ambiente) configurado na raiz do projeto, basta rodar os seguintes comandos no seu terminal:

```bash
    # Você deve estar no diretório do projeto onde está o arquivo package.json

    # Instalar as dependências
    $ npm install
    # Rodar
    $ npm run dev
```

- Se tudo funcionou corretamente você pode acessar a plataforma pelo seu browser no endereço **<http://localhost:5173/>**