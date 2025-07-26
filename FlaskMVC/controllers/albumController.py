from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.albumModel import *

albumsBP = Blueprint('albums',__name__)

#Ruta de inicio
@albumsBP.route('/')
def home():
    try:
        consultaTodo = getAll()
        return render_template('formulario.html', errores={},albums=consultaTodo)
    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template('formulario.html', errores={}, albums=[])
    
#Ruta de detalles
@albumsBP.route('/detalles/<int:id>')
def detalle(id):
    try:
        consultaId = getById(id)
        return render_template('consulta.html', Albums=consultaId)
    except Exception as e:
        print('Error al consultar por id:' +e)
        return redirect(url_for('albums.home'))

#Ruta de guardar
@albumsBP.route('/guardarAlbum', methods=['POST'])
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
            insertAlbum(titulo,artista,anio)
            flash('Album guardado en BD')
            return redirect(url_for('albums.home')) 
        
        except Exception as e:
            mysql.connection.rollback()
            flash ('Error al guardar: ' + str(e))
            return redirect(url_for('home')) 

    return render_template('formulario.html', errores=errores)

#Ruta de editar (abre form)
@albumsBP.route('/editar/<int:id>')
def editar(id):
    try:
        consultaId = getById(id)
        return render_template('formUpdate.html', album=consultaId)
    except Exception as e:
        print('Error al obtener álbum:', e)
        return redirect(url_for('albums.home'))
    
#Ruta de actualizar
@albumsBP.route('/actualizarAlbum/<int:id>', methods=['POST'])
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
        updateAlbum(id,titulo,artista,año)
        flash('Álbum actualizado correctamente')
    except Exception as e:
        mysql.connection.rollback()
        flash('Error al actualizar: ' + str(e))

    return redirect(url_for('albums.home'))

#Ruta de eliminar (formulario)
@albumsBP.route('/eliminar/<int:id>')
def confirmarEliminacion(id):
    try:
        consultaId = getById(id)
        return render_template('confirmDel.html', album=consultaId)
    except Exception as e:
        flash('Error: ' + str(e))
        return redirect(url_for('albums.home'))

# Ejecutar eliminar
@albumsBP.route('/confirmacion/<int:id>', methods=['POST'])
def eliminarAlbum(id):
    try:
        softDeleteAlbum(id)
        flash('Álbum eliminado correctamente')
    except Exception as e:
        mysql.connection.rollback()
        flash('Error: ' + str(e))
    return redirect(url_for('albums.home'))
