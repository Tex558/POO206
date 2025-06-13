
from flask import Flask

app = Flask(__name__)

#Ruta simple
@app.route('/')
def home():
    return 'Hola Mundo FLASK'

#Ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Un saludo a la grasa '+ nombre +'!'

#Ruta try-catch
@app.errorhandler(404)
def PagNoE(e):
    return 'EY! Aprenda a escribir Lerdo :)'

#Ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Soy el mismo recurso en diferente pagina ;)'

#Ruta POST
@app.route('/formulario', methods=['POST'])
def formulario():
    return 'Soy un fomrulario'

if __name__ == '__main__':
    app.run(port=3000, debug=True)