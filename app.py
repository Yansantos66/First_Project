import serverless_wsgi 
import requests
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_s3 import FlaskS3 
from datetime import datetime, timedelta
import boto3
import logging 

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
logging.info("Homepage success")

@app.route("/cadastramento", methods=["POST", "GET"])
def cadastro():
    try:
        ncliente = request.form.get("nome")
        if request.method == "POST":

            ncliente = request.form["nome"]
            cpfcliente = request.form["cpf"]
            datcliente = request.form["data"]
            celcliente = request.form["celular"]
            data_minima = datetime.now() - timedelta(days=18 * 365)
            idade_cliente = datetime.strptime(datcliente, "%Y-%m-%d")
            idade_permitida = idade_cliente < data_minima
            logging.info("informação capturadas com sucesso")
            dynamodb = boto3.resource("dynamodb")
            table = dynamodb.Table('clientes')
            

            response = table.get_item(Key={
            'cpf': cpfcliente
            })
            logging.info("Pegando informações")
            if "Item" in response: 
                flash(f"Cliente {ncliente} já cadastrado com esses dados!")
            elif idade_permitida:                       
                response = table.put_item(
                        Item={
                            'nome': ncliente,
                            'cpf': cpfcliente,
                            'data': datcliente,
                            'celular': celcliente
                        }
                        )
                logging.info("Adicionando informações no dynamodb")

                flash("Cliente cadastrado com sucesso! Agora você faz parte do time PagBank PagSeguro!")
            else:
                flash("Analisamos que você ainda não tem idade mínima permitida, e por isso não podemos prosseguir com seu cadastro. ")
            return render_template("conta.html")
    except Exception as e:
        print("ERRO " + str(e))
        return response 
        
    return render_template("conta.html")

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
#if __name__ == "__main__":
#    app.run(debug=True)
#clientes = [
    #  {"nome": "", "cpf": "", "data": "", "celular": ""},
    #  {"nome": "", "cpf": "", "data": "", "celular": ""},
