
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Emiliano04'
app.config['MYSQL_DB'] = 'dbflask'

mysql = MySQL(app)

@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500


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