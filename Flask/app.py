
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
        cursor.execute('SELECT * FROM albums WHERE state = 1')
        consultaTodo= cursor.fetchall()
        return render_template('formulario.html', errores={}, albums=consultaTodo)

    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template('formulario.html', errores={}, albums=[])

    finally:
        cursor.close()

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

#Rta de editar
@app.route('/editar/<int:id>')
def editar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM Albums WHERE id=%s', (id,))
        album = cursor.fetchone()
        return render_template('formUpdate.html', album=album)
    except Exception as e:
        print('Error al obtener álbum:', e)
        return redirect(url_for('home'))
    finally:
        cursor.close()

#Ruta de actualizar
@app.route('/actualizarAlbum/<int:id>', methods=['POST'])
def actualizarAlbum(id):
    datos = request.form
    titulo = datos.get('txtTitulo', '').strip()
    artista = datos.get('txtArtista', '').strip()
    año = datos.get('txtAnio', '').strip()
    errores = {}

    if not titulo:
        errores['txtTitulo'] = 'El título es obligatorio'
    if not artista:
        errores['txtArtista'] = 'El artista es obligatorio'
    if not año:
        errores['txtAnio'] = 'El año es obligatorio'
    elif not año.isdigit() or int(año) < 1800 or int(año) > 2030:
        errores['txtAnio'] = 'Ingrese un año válido'

    if errores:
        return render_template('formUpdate.html', album=(id, titulo, artista, año), errores=errores)

    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE Albums SET Titulo=%s, Artista=%s, Año=%s WHERE id=%s', (titulo, artista, año, id))
        mysql.connection.commit()
        flash('Álbum actualizado correctamente')
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
        cursor.execute('SELECT * FROM Albums WHERE id=%s', (id,))
        album = cursor.fetchone()
        if not album:
            flash('Álbum no encontrado')
            return redirect(url_for('home'))
        return render_template('confirmDel.html', album=album)
    except Exception as e:
        flash('Error: ' + str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()

# Ejecutar eliminar
@app.route('/confirmacion/<int:id>', methods=['POST'])
def eliminarAlbum(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE Albums SET state = 0 WHERE id=%s', (id,))
        mysql.connection.commit()
        flash('Álbum eliminado correctamente')
    except Exception as e:
        mysql.connection.rollback()
        flash('Error: ' + str(e))
    finally:
        cursor.close()
    return redirect(url_for('home'))

#Ruta de insert
@app.route('/guardarAlbum', methods=['POST'])
def guardar():

    errores = {}

    titulo = request.form.get('txtTitulo','').strip()
    artista = request.form.get('txtArtista','').strip()
    anio = request.form.get('txtAnio','').strip()

    if not titulo:
        errores['txtTitulo'] = 'Nombre del album obligatorio'
    if not artista:
        errores['txtArtista'] = 'Nombre del artista obligatorio'
    if not anio:
        errores['txtAnio'] = 'Falta el año del album'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
        errores['txtAnio'] = 'Ingresar un año valido'
        
    if not errores:

        try:
            cursor= mysql.connection.cursor()
            cursor.execute('insert into albums(Titulo,Artista,Año) values(%s,%s,%s)',(titulo, artista, anio))
            mysql.connection.commit()
            flash('Album guardado en BD')
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