from flask import Flask
from flask import request
from flask import redirect
from flask import session
from flask import render_template

from database import select_query, modify_query

app = Flask(__name__, template_folder="app/templates")

app.secret_key = "qwertyuiop"

@app.route("/", methods=["GET"])
def index():
    if "username" in session:
        title = "Página principal"
        return render_template("index.html", title=title, username=session["username"])
    else:
        title = "Por favor inicie sesión"
        return render_template("login.html", title=title)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method != "POST":
        return index()
    else:
        username = request.form["username"]
        email    = request.form["email"]
        password = request.form["password"]

        # Guarda el registro en la DB
        modify_query(f"insert into user_table (username, email, password) values ('{username}', '{email}', '{password}')")

        # Registra la sesión
        session["username"] = username

        return index()


@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return index()
    else:
        title = "Inicio de Sesion"
        return render_template("login.html", title=title)

@app.route("/register", methods=["GET", "POST"])
def register():
    if "username" in session:
        return index()
    else:
        title = "Regístrese"
        return render_template("register.html", title=title)


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method != "POST":
        return index()
    else:
        username = request.form["username"]
        password = request.form["password"]

        result = select_query(f"select email, password from user_table where username='{username}'")

        print("Resultado de la query: " + str(result))

        if result:
            if result[0][1] == password:
                # Registra la sesión
                session["username"] = username
            else:
                print("password incorrecto")
        else:
            print("usuario no registrado")
        return index()


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return index()


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Página no encontrada...<h1>"


if __name__ == "__main__":
    app.run(debug=True)