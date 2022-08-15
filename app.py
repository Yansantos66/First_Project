import requests
from re import A
from flask import Flask, render_template, request, url_for, json, flash, redirect
from datetime import datetime, timedelta

#Framework
#Lista de dicionários 
#Percorrer lista
#Verificar igualdade e gerar conflito
clientes = [
    {
        "nome": "Yan Santos",
        "cpf": "123.456.789-12",
        "data": "2004-08-12",
        "celular": "(11)+12345-6789",
    },
    {
        "nome": "Yan Santos",
        "cpf": "123.456.789-12",
        "data": "2004-08-12",
        "celular": "(11)+12345-6789",
    },
]
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


@app.route("/cadastramento", methods=["POST", "GET"])
def cadastro():
    ncliente = request.form.get("nome")
    if request.method == "POST":
        ncliente = request.form["nome"]
        cpfcliente = request.form["cpf"]
        datcliente = request.form["data"]
        celcliente = request.form["celular"]
        data_minima = datetime.now() - timedelta(days=18 * 365)
        idade_cliente = datetime.strptime(datcliente, "%Y-%m-%d")#formato de data
        idade_permitida = idade_cliente < data_minima 
        if idade_permitida:
            clientes.append(
                {
                    "nome": ncliente,
                    "cpf": cpfcliente,
                    "data": datcliente,
                    "celular": celcliente,
                }
            )
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
























