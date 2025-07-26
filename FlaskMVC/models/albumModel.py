from app import mysql 

#metodo para obtener albums activos
def getAll():        
    cursor= mysql.connection.cursor()
    cursor.execute('SELECT * FROM albums WHERE state = 1')
    consultaTodo= cursor.fetchall()
    cursor.close()
    return consultaTodo

#metodo para obtener album por id
def getById(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM Albums WHERE id=%s', (id,))
    consultaId = cursor.fetchone()
    cursor.close()
    return consultaId

#metodo para guardar album por id
def insertAlbum(titulo,artista,anio):
    cursor= mysql.connection.cursor()
    cursor.execute('insert into albums(Titulo,Artista,Año) values(%s,%s,%s)',(titulo, artista, anio))
    mysql.connection.commit()
    cursor.close()

#metodo para editar album por id
def updateAlbum(id,titulo,artista,año):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE Albums SET Titulo=%s, Artista=%s, Año=%s WHERE id=%s', (titulo, artista, año, id))
    mysql.connection.commit()
    cursor.close()

#metodo para eliminar album por id
def softDeleteAlbum(id):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE Albums SET state = 0 WHERE id=%s', (id,))
    mysql.connection.commit()
    cursor.close()

#Base de datos
def probarBD():
    cursor= mysql.connection.cursor()
    cursor.execute('Select 1')
    cursor.close()