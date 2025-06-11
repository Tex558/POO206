
from flask import Flask

app = Flask(__name__)

#Añadir ruta
@app.route('/')
def home():
    return 'Hola Mundo FLASK'

if __name__ == '__main__':
    app.run(port=3000, debug=True)