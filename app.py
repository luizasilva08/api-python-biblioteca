# desenvolver um back end com api - 
# postman - teste http -> verificar respostas da API
# 1. OBJETIVO
# 2. URLBASE
# 3. ENDPOINTS
# 4. RECURSOS DISPONIBILIZADOS

#VAMOS CRIAR UMA API:

"""
1. CONSULTAR
2. CRIAR
3. EDITAR
4. EXCLUIR
C.R.U.D
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
#APP -> REPRESENTA A APLICAÇÃO FLASK
#__NAME__ -> IDENTIFICA QUE O MODULO DA APLICAÇÃO

livros = [
    {"id":1,
     "titulo":"A Hora da Estrela",
     "autor": "Clarice Lispector"
    },

    {"id":2,
     "titulo":"Orgulho e Preconceito",
     "autor":"Jane Austen"
    },

    {"id":3,
     "titulo": "Crime e Castigo",
     "autor": "Fiodor Dostoievski"
    },

     {"id":4,
     "titulo":"Dom Casmurro",
     "autor":"Machado de Assis"
    },

    {"id":5,
     "titulo":"Grande Sertão: Veredas",
     "autor":"João Guimarães Rosa"
    },

    {"id":6,
     "titulo":"1984",
     "autor":"George Orwell"
    },

    {"id":7,
     "titulo":"Cem Anos de Solidão",
     "autor":"Gabriel García Márquez"
    },

    {"id":8,
     "titulo":"O Pequeno Príncipe",
     "autor":"Antoine de Saint-Exupéry"
    },

    {"id":9,
     "titulo":"Memórias Póstumas de Brás Cubas",
     "autor":"Machado de Assis"
    },

    {"id":10,
     "titulo":"O Senhor dos Anéis",
     "autor":"J. R. R. Tolkien"
    },

    {"id":11,
     "titulo":"Capitães da Areia",
     "autor":"Jorge Amado"
    },

    {"id":12,
     "titulo":"Vidas Secas",
     "autor":"Graciliano Ramos"
    },

    {"id":13,
     "titulo":"Fausto",
     "autor":"Johann Wolfgang von Goethe"
    }
]


#CONSULTAR LIVROS - CRIAR UMA FUNÇÃO

#def obter_livros():
    #return jsonify(livros)

#CRIAR AS ROTAS /LIVROS
#a rota foi especificada, somente o método GET 
#será aceito

@app.route("/livros", methods = ["GET"])
def obter_livros():
    return jsonify(livros)

#CRIAR AS ROTAS /LIVROSid
@app.route("/livros/<int:id>", methods=["GET"])
#<int:> -> indica inteiro
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
    return jsonify({"message":"LIVRO NAO ENCONTRADO"}), 404

#PUT -> primeiro, os dados enviados pelo cliente
#serão obtidos 
@app.route ("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):
    #permite acessar os dados json enviados no corpo (body)
    #da requisição
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id")==id:
            livros[indice].update(livro_alterado)
            return jsonify(livro[indice])

#CRIAÇÃO DE UM NOVO LIVRO
#decorador de rota
@app.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#delete-excluir um livro

@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    #como é necessário remover um elemento da lista
    #pelo seu índice, será utilizado novamente o 
    #enumerate()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)










    


#INICIALIZAÇÃO DO SERVIDOR LOCAL
app.run(
    host="localhost", 
    port=5000,
    debug=True
)