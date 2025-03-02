from flask import Flask, request, render_template

app = Flask(__name__)

from controllers.usuario_controller import *



@app.route("/error", methods=['GET','POST'])
def erros():
    return render_template("erro.html")

@app.route('/index', methods=['POST'])
def index():
    login = request.form['login']
    password = request.form['password']
   # print(login,password)
    if login == "mateus@ifce.edu.br" and password == "1234":
        return render_template("index.html")
    else:
        return render_template("erro.html")


@app.route('/soma', methods=['GET'])
def soma():
    a = request.args.get("a")
    b = request.args.get("b")
    if (a is not None and b is not None):
        return str(int(a) + int(b))
    return "paramentros faltando"


@app.route('/sub', methods=['GET'])
def sub():
    a = request.args.get("a")
    b = request.args.get("b")
    if (a is not None and b is not None):
        return str(int(a) - int(b))
    return "paramentros faltando"


if __name__ == '__main__':
    app.run(debug=True)
