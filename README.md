# API Python – Biblioteca

API REST desenvolvida em **Python** com o framework **Flask**, que implementa as operações de **CRUD** (Create, Read, Update, Delete) sobre um catálogo de livros. Projeto de caráter acadêmico, voltado ao aprendizado de desenvolvimento *back-end* e ao teste de requisições HTTP com o Postman.

## Sumário

- [Objetivo](#objetivo)
- [Tecnologias](#tecnologias)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e execução](#instalação-e-execução)
- [URL base](#url-base)
- [Endpoints](#endpoints)
- [Exemplos de uso](#exemplos-de-uso)
- [Modelo de dados](#modelo-de-dados)
- [Limitações conhecidas](#limitações-conhecidas)
- [Autoria](#autoria)

## Objetivo

Disponibilizar uma API simples para gerenciar uma biblioteca, permitindo:

1. **Consultar** a lista de livros ou um livro específico;
2. **Criar** um novo livro;
3. **Editar** os dados de um livro existente;
4. **Excluir** um livro.

## Tecnologias

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Postman](https://www.postman.com/) (para testes das requisições HTTP)

## Estrutura do repositório

```
api-python-biblioteca/
├── app.py        # Aplicação Flask: dados, rotas e inicialização do servidor
└── README.md     # Documentação do projeto
```

## Pré-requisitos

- Python 3.8 ou superior
- `pip` (gerenciador de pacotes do Python)

## Instalação e execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/luizasilva08/api-python-biblioteca.git
   cd api-python-biblioteca
   ```

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux / macOS
   source venv/bin/activate
   ```

3. Instale a dependência:

   ```bash
   pip install flask
   ```

4. Execute a aplicação:

   ```bash
   python app.py
   ```

O servidor será iniciado em modo de depuração (`debug=True`) e ficará disponível em `http://localhost:5000`.

## URL base

```
http://localhost:5000
```

## Endpoints

| Método   | Rota            | Descrição                          | Corpo da requisição |
|----------|-----------------|------------------------------------|---------------------|
| `GET`    | `/livros`       | Lista todos os livros              | —                   |
| `GET`    | `/livros/<id>`  | Retorna um livro pelo `id`         | —                   |
| `POST`   | `/livros`       | Cadastra um novo livro             | JSON                |
| `PUT`    | `/livros/<id>`  | Edita os dados de um livro         | JSON                |
| `DELETE` | `/livros/<id>`  | Exclui um livro pelo `id`          | —                   |

### Respostas

- `GET /livros` → lista completa de livros em JSON.
- `GET /livros/<id>` → objeto JSON do livro; caso o `id` não exista, retorna `404` com a mensagem `{"message": "LIVRO NAO ENCONTRADO"}`.
- `POST /livros` → retorna a lista atualizada de livros.
- `DELETE /livros/<id>` → retorna a lista atualizada de livros.

## Exemplos de uso

Os exemplos abaixo utilizam `curl`; as mesmas requisições podem ser realizadas no Postman.

**Listar todos os livros**

```bash
curl http://localhost:5000/livros
```

**Consultar um livro por id**

```bash
curl http://localhost:5000/livros/1
```

**Cadastrar um novo livro**

```bash
curl -X POST http://localhost:5000/livros \
  -H "Content-Type: application/json" \
  -d '{"id": 14, "titulo": "O Cortiço", "autor": "Aluísio Azevedo"}'
```

**Editar um livro**

```bash
curl -X PUT http://localhost:5000/livros/14 \
  -H "Content-Type: application/json" \
  -d '{"titulo": "O Cortiço (Edição Revisada)"}'
```

**Excluir um livro**

```bash
curl -X DELETE http://localhost:5000/livros/14
```

## Modelo de dados

Cada livro é representado por um objeto JSON com os seguintes campos:

| Campo    | Tipo    | Descrição                  |
|----------|---------|----------------------------|
| `id`     | inteiro | Identificador do livro     |
| `titulo` | texto   | Título da obra             |
| `autor`  | texto   | Nome do autor              |

Exemplo:

```json
{
  "id": 1,
  "titulo": "A Hora da Estrela",
  "autor": "Clarice Lispector"
}
```

## Limitações conhecidas

- Os dados são armazenados **em memória** (lista Python); ao reiniciar o servidor, todas as alterações são perdidas.
- Não há validação dos dados enviados nem verificação de `id` duplicado no cadastro.
- Não há autenticação.

## Autoria

Desenvolvido por [Luíza da Silva](https://github.com/luizasilva08).
