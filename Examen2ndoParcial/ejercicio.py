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
        cursor.execute('SELECT * FROM peliculas WHERE Estado = 1')
        consultaTodo= cursor.fetchall()
        return render_template('formulario.html', errores={}, peliculas=consultaTodo)

    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template('formulario.html', errores={}, peliculas=[])

    finally:
        cursor.close()

#Ruta de detalle
@app.route('/detalles/<int:id>')
def detalles(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM peliculas WHERE id=%s', (id,))
        consultaId = cursor.fetchone()
        return render_template('consulta.html', peliculas=consultaId)
    except Exception as e:
        print('Error al consultar por id:' +e)
        return redirect(url_for('home'))
    finally:
        cursor.close()

#Rta de editar
@app.route('/editar/<int:id>')
def editar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM Peliculas WHERE id=%s', (id,))
        pelicula = cursor.fetchone()
        return render_template('actualizar.html', pelicula=pelicula)
    except Exception as e:
        print('Error al obtener pelicula:', e)
        return redirect(url_for('home'))
    finally:
        cursor.close()

#Ruta de actualizar
@app.route('/actualizarPeli/<int:id>', methods=['POST'])
def actualizarPeli(id):
    datos = request.form
    titulo = datos.get('txtTitulo', '').strip()
    director = datos.get('txtDirector', '').strip()
    año = datos.get('txtAnio', '').strip()
    genero = datos.get('txtGenero', '').strip()
    errores = {}

    if not titulo:
        errores['txtTitulo'] = 'El título es obligatorio'
    if not director:
        errores['txtDirector'] = 'El Director es obligatorio'
    if not año:
        errores['txtAnio'] = 'El año es obligatorio'
    elif not año.isdigit() or int(año) < 1800 or int(año) > 2030:
        errores['txtAnio'] = 'Ingrese un año válido'
    if not genero:
        errores['txtGenero'] = 'El genero es obligatorio'

    if errores:
        return render_template('actualizar.html', pelicula=(id, titulo, director, año, genero), errores=errores)

    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE peliculas SET Titulo=%s, Director=%s, Año=%s, Genero=%s WHERE id=%s', (titulo, director, año, genero, id))
        mysql.connection.commit()
        flash('Pelicula actualizada correctamente')
    except Exception as e:
        mysql.connection.rollback()
        flash('Error al actualizar: ' + str(e))
    finally:
        cursor.close()

    return redirect(url_for('home'))

#Ruta de eliminar
@app.route('/eliminar/<int:id>')
def confirmarEliminacion(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM peliculas WHERE id=%s', (id,))
        pelicula = cursor.fetchone()
        if not pelicula:
            flash('Pelicula no encontrada')
            return redirect(url_for('home'))
        return render_template('borrar.html', pelicula=pelicula)
    except Exception as e:
        flash('Error: ' + str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()

# Ejecutar eliminar
@app.route('/confirmacion/<int:id>', methods=['POST'])
def eliminarPelicula(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE peliculas SET Estado = 0 WHERE id=%s', (id,))
        mysql.connection.commit()
        flash('Pelicula eliminada correctamente')
    except Exception as e:
        mysql.connection.rollback()
        flash('Error: ' + str(e))
    finally:
        cursor.close()
    return redirect(url_for('home'))

#Ruta de insert
@app.route('/guardarPeli', methods=['POST'])
def guardar():

    errores = {}

    titulo = request.form.get('txtTitulo','').strip()
    director = request.form.get('txtDirector','').strip()
    anio = request.form.get('txtAnio','').strip()
    genero = request.form.get('txtGenero','').strip()

    if not titulo:
        errores['txtTitulo'] = 'Nombre de la pelicula obligatorio'
    if not director:
        errores['txtDirector'] = 'Nombre del director obligatorio'
    if not anio:
        errores['txtAnio'] = 'Falta el año de la pelicula'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
        errores['txtAnio'] = 'Ingresar un año valido'
    if not genero:
        errores['txtGenero'] = 'El genero es obligatorio'
        
    if not errores:

        try:
            cursor= mysql.connection.cursor()
            cursor.execute('insert into peliculas(Titulo,Director,Año,Genero) values(%s,%s,%s,%s)',(titulo, director, anio, genero))
            mysql.connection.commit()
            flash('Pelicula guardada en BD')
            return redirect(url_for('home')) 
        
        except Exception as e:
            mysql.connection.rollback()
            flash ('Error al guardar: ' + str(e))
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