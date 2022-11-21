import serverless_wsgi 
import requests
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_s3 import FlaskS3 
from datetime import datetime, timedelta
import boto3

app = Flask(__name__, static_folder='static')
app.config["SECRET_KEY"] = "key_secret"
app.config['FLASKS3_BUCKET_NAME'] = 'bucket-storage' 
s3 = FlaskS3() 
s3.init_app(app)

@app.context_processor
def inject_static_url():
    return dict(
        static_url='https://bucket-storage.s3.sa-east-1.amazonaws.com/'
    )

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/cadastramento", methods=["POST", "GET"])
def cadastro():
    ncliente = request.form.get("nome")
    if request.method == "POST":

        ncliente = request.form["nome"]
        cpfcliente = request.form["cpf"]
        datcliente = request.form["data"]
        celcliente = request.form["celular"]

        data_minima = datetime.now() - timedelta(days=18 * 365)
        idade_cliente = datetime.strptime(datcliente, "%Y-%m-%d")
        idade_permitida = idade_cliente < data_minima

        response = self.table.get_item(Key={
        'cpf': cpfcliente, 
        'celular': celcliente
        })
        for cliente in clientes:
            if cliente['cpf'] == cpfcliente or cliente['celular'] == celcliente: 
                flash(f"Cliente {ncliente} já cadastrado com esses dados!")
                return render_template("conta.html")
        return response 
    if idade_permitida: 
        clientes.append=({
            'nome': ncliente, 
            'cpf': cpfcliente, 
            'data': datcliente, 
            'celular': celcliente
            }
        )
def put_user(ncliente, cpfcliente, datcliente, celcliente, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Users')
        response = table.put_item(
        Item={
            'nome': ncliente,
            'cpf': cpfcliente,
            'data': datcliente,
            'celular': celcliente
           }
        )  
        return response    
        flash("Cliente cadastrado com sucesso! Agora você faz parte do time PagBank PagSeguro!")
    else:
        flash("Analisamos que você ainda não tem idade mínima permitida, e por isso não podemos prosseguir com seu cadastro. ")
    return render_template("conta.html")

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
#if __name__ == "__main__":
#    app.run(debug=True)
clientes = [
    {"nome": "", "cpf": "", "data": "", "celular": ""},
    {"nome": "", "cpf": "", "data": "", "celular": ""},
]