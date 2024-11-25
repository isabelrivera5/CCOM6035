from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('Login.html')

@app.route("/buscar")
def buscar():
    return render_template('Buscador.html')

@app.route("/agregar")
def agregar():
    return render_template('Agregar.html')

@app.route("/principal")
def principal():
    return render_template('Principal.html')

if __name__ == '__main__':
    app.run(debug=True)
