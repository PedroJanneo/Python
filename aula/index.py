from flask import Flask, render_template

# a varial abaixo é a variavel
# que roda a aplicacao (todos
#os objetos de projeto depende dela)


app = Flask(__name__)

@app.route('/inicio')
def ola():
    return'<h1> Iniciando flask</h1>'


@app.route('/lista')
def lista():
    return render_template('lista.html')

app.run()