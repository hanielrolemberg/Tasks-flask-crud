from flask import Flask

#quando executado de forma manual, esse name tem valor de main, deste modo:
#__name__ = "__main__" 
app = Flask(__name__) #string/variável criada . Esse name é para ser o nome do arquivo
#criando a rota - criar comunicação - enviar e receber info

@app.route("/") #criando o endpoint @app é variável e route é o método. Essa barra é indicando o diretório. Nesse caso, é o principal
#quando alguém acessar essa rota, vai acessar:
def hello_world():
    return "Hello world!"

@app.route("/about")
def about():
    return "Página sobre" 

#para fazer funcionar:

if __name__ == "__main__": #Garante que se esse arquivo for subido de modo manual, vamos subir o servidor desta forma (pois aqui é mais usado no ambiente de homologação, isto é, desenvolvimento local - app.run(debug=True))
    app.run(debug=True) #debug é uma propriedade que nos permite visualizar informações que vão nos ajudar a entender o que está acontecendo no servidor web

   