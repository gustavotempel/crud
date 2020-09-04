from flask import Flask
from flask import request
from flask import redirect
from flask import session
from flask import render_template

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from database import select_query
from database import modify_query

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

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
        username = request.form.get("username").lower()
        email    = request.form.get("email").lower()
        password = generate_password_hash(request.form.get("password"))

        # Verifica si ya existe usuario y email
        db_username = select_query(f"select username from users where username='{username}'")
        db_email = select_query(f"select email from users where username='{email}'")

        if db_username or db_email:
            print("Usuario o email existente")
            return index()
        elif request.form.get("password") == request.form.get("password2") :
            # Guarda el registro en la DB
            modify_query(f"insert into users (username, email, password) values ('{username}', '{email}', '{password}')")

            # Registra la sesión
            session["username"] = username

        return index()

@app.route("/validatefield")
def validatefield():
    print(request)
    field = request.args.get("field")
    value = request.args.get("value")
    print(value)
    result = select_query(f"select {field} from users where {field}='{value}'")
    if result:
        print("Usuario/email ya registado")
        return "Used"
    else:
        print("Usuario y email disponibles")
        return "Available"


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
        username = request.form.get("username").lower()
        password = request.form.get("password")

        result = select_query(f"select email, password from users where username='{username}'")

        print("Resultado de la query: " + str(result))

        if result:
            if check_password_hash(result[0][1], password):
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