
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


#Ruta principal
@app.route('/')
def home():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT * FROM albums')
        consultaTodo= cursor.fetchall()
        return render_template('formulario.html', errores={}, albums=consultaTodo)

    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template('formulario.html', errores={}, albums=[])

    finally:
        cursor.close()

#Ruta con parametros
#@app.route('/saludo/<nombre>')
    #return 'Un saludo a la grasa '+ nombre +'!'

#Ruta de detalle
@app.route('/detalles/<int:id>')
def detalle(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM Albums WHERE id=%s', (id,))
        consultaId = cursor.fetchone()
        return render_template('consulta.html', Albums=consultaId)
    except Exception as e:
        print('Error al consultar por id:' +e)
        return redirect(url_for('home'))
    finally:
        cursor.close()

#Ruta insert
@app.route('/guardarAlbum', methods=['POST'])
def guardar():

    errores = {}

    #obtenen datos al ingresar
    titulo = request.form.get('txtTitulo','').strip()
    artista = request.form.get('txtArtista','').strip()
    anio = request.form.get('txtAnio','').strip()

    #manejo de campos vacios
    if not titulo:
        errores['txtTitulo'] = 'Nombre del album obligatorio'
    if not artista:
        errores['txtArtista'] = 'Nombre del artista obligatorio'
    if not anio:
        errores['txtAnio'] = 'Año del album obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
        errores['txtAnio'] = 'En año solo ingresar un año valido'
        
    if not errores:
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
    return render_template('formulario.html', errores=errores)

#Ruta try-catch
@app.errorhandler(404)
def PagNoE(e):
    return 'EY! Aprenda a escribir :)'

@app.errorhandler(405)
def PagNoE(e):
    return 'EY! Revisa el metodo de envio :)'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)