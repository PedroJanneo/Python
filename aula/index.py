from flask import Flask, render_template

# a varial abaixo é a variavel
# que roda a aplicacao (todos
#os objetos de projeto depende dela)
#pip install flask

class Produto:
    def __init__(self, nome_prod, marca_prod, preco_prod):
            self.nome = nome_prod 
            self.marca = marca_prod
            self.preco = preco_prod

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return'<h1> Iniciando flask</h1>'


@app.route('/lista')
def lista():
    # a linha abaixo instancia um novo produto 
    prod01 = Produto("Camisa", "NIKE", "R$ 300,00")
    prod02 = Produto("Blusa", "Lacoste", "R$ 255,00")
    prod03 = Produto("Calça", "Oakley", "r$ 200,00")
    
    
    produtos_cadastrados = [prod01, prod02, prod03]
    return render_template('lista.html', descricao = "Aqui estão seus produtos cadastrados", lista_prod = produtos_cadastrados)

app.run()