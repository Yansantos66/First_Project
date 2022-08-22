import requests
from flask import Flask, render_template, request, url_for, flash, redirect
from datetime import datetime, timedelta
import json
#Framework
#Lista de dicionários 
with open('dados.json') as jsonfile:    #Leitura do arquivo Json 
    clientes = json.load(jsonfile)


app = Flask(__name__)
app.config["SECRET_KEY"] = "key_secret"

# route
# função
# template
@app.route("/")
def homepage():
    return render_template("index.html")


# aceitar somente letras no campo nome
# se caso houver uma ação inesperada como número, parar o code e inserir uma mensagem
# Caso houver uma ação esperada continuar o code


@app.route("/cadastramento", methods=["POST", "GET"])             #Criar um dado/atualizar  #Pegar informação
def cadastro():
    ncliente = request.form.get("nome")
    if request.method == "POST":        #Verificando o metodo
        
        ncliente = request.form["nome"]         #Pegando informações do cliente(FRONT-END)
        cpfcliente = request.form["cpf"]        
        datcliente = request.form["data"]
        celcliente = request.form["celular"]

        data_minima = datetime.now() - timedelta(days=18 * 365)     #Calculo
        idade_cliente = datetime.strptime(datcliente, "%Y-%m-%d")   #formato de data
        idade_permitida = idade_cliente < data_minima 
        
        for cliente in clientes:                                                            #Percorrer lista
                if cliente ["cpf"] == cpfcliente or cliente["celular"] == celcliente:       #Verificar igualdade e gerar conflito
                    flash("Cliente já cadastrado")
                    return render_template("conta.html") 
        
        if idade_permitida:   
            clientes.append(
                {
                    "nome": ncliente,
                    "cpf": cpfcliente,
                    "data": datcliente,
                    "celular": celcliente,
                }
            )
        
            with open('dados.json', 'w') as jsonadd:        #adicionar dados no Json 
                json.dump(clientes, jsonadd, indent=4)

            flash("Cliente cadastrado com sucesso. Agora você faz parte do time PagBank PagSeguro!")
        else:
            flash("Vimos que você ainda é menor de idade e por isso, não conseguimos prosseguir com seu cadastro.")
    return render_template("conta.html")


if __name__ == "__main__":
    app.run(debug=True)

    clientes = [
        {"nome": "", "cpf": "", "data": "", "celular": ""},
        {"nome": "", "cpf": "", "data": "", "celular": ""},
    ]



