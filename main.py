from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder = "app/templates")

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/', methods = ['GET', 'POST'])
def index():
    title = "Primera página de Prueba"
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

