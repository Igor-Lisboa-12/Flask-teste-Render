from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '🚀 Aplicação Flask funcionando no Render!'

@app.route('/html')
def pagina_html():
    return render_template('pagina.html')


if __name__ == '__main__':
    app.run(debug=True)
