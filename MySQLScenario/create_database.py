import mysql.connector
from mysql.connector import errorcode

def Create_database():
    # Conectar a MySQL
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='brownsquid',  # Reemplaza con tu usuario de MySQL
            password='123QAZwsx!'  # Reemplaza con tu contraseña de MySQL
        )
        cursor = cnx.cursor()
        print("Conexión a MySQL exitosa.")

        # Crear base de datos
        cursor.execute("CREATE DATABASE IF NOT EXISTS MELIChallenge")
        print("Base de datos 'MELIChallenge' creada exitosamente.")

    except:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está mal con tu usuario o contraseña.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe.")
        else:
            print(err)
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("Conexión a MySQL cerrada.")

if __name__ == "__main__":
    Create_database()