from flask import Blueprint, jsonify
from app import mysql
import MySQLdb

internoBP = Blueprint('intern',__name__)

@internoBP.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500

#Ruta try-catch
@internoBP.errorhandler(404)
def PagNoE(e):
    return 'EY! Aprenda a escribir :)'

@internoBP.errorhandler(405)
def PagNoE(e):
    return 'EY! Revisa el metodo de envio :)'
