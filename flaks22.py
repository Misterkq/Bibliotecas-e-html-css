from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("login.html") 

@app.route("/processar_cadastro", methods=["POST"]) 
def processar_cadastro():
    nome = request.form.get("nome_usuario")
    senha = request.form.get("senha")

    print(f"Novo usuario: {nome} e senha: {senha}")


    return redirect(url_for("boas_vinda"))

@app.route("/bem-vindo")
def boas_vinda():
    return render_template("home_page.html")

if __name__ == '__main__':
    app.run(debug=True)