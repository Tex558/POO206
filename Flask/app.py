
from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Emiliano04'
app.config['MYSQL_DB'] = 'dbflask'

app.secret_key ='mysecretkey'

mysql = MySQL(app)

@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500


#Ruta principal y de consulta
@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Ruta insert
@app.route('/guardarAlbum', methods=['POST'])
def guardar():

    #obtenen datos al ingresar
    titulo = request.form.get('txtTitulo','').strip()
    artista = request.form.get('txtArtista','').strip()
    anio = request.form.get('txtAnio','').strip()

    #Intentar ejecutar el insert
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('insert into albums(Titulo,Artista,Año) values(%s,%s,%s)',(titulo, artista, anio))
        mysql.connection.commit()
        flash('Album guardado en BD')
        return redirect(url_for('home')) 
    
    except Exception as e:
        mysql.connection.rollback()
        flash ('Error al guardar BD: ' + str(e))
        return redirect(url_for('home')) 

    finally:
        cursor.close()

#Ruta try-catch
@app.errorhandler(404)
def PagNoE(e):
    return 'EY! Aprenda a escribir :)'

@app.errorhandler(405)
def PagNoE(e):
    return 'EY! Revisa el metodo de envio :)'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)