import mysql.connector
from mysql.connector import errorcode

def Create_tables():
    # Conectar a MySQL
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='brownsquid',  # Reemplaza con tu usuario de MySQL
            password='123QAZwsx!'  # Reemplaza con tu contraseña de MySQL
        )
        cursor = cnx.cursor()
        print("Conexión a MySQL exitosa.")

        # Conectar a la base de datos creada
        cnx.database = 'MELIChallenge'

        # Lista de tablas a borrar
        tables_to_delete = ["events","campaigns","customers"]

        # Borrado de cada tabla
        for table in tables_to_delete:
            sql = f"DROP TABLE IF EXISTS {table}"
            try:
                # Ejecutar la consulta
                cursor.execute(sql)
                print(f"La tabla '{table}' ha sido borrada.")
            except Exception as e:
                print(f"Error al borrar la tabla '{table}': {e}")
        

        # Crear tabla 'customers'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id SMALLINT PRIMARY KEY,
                first_name VARCHAR(64),
                last_name VARCHAR(64)
            )
        """)
        print("Tabla 'customers' creada exitosamente.")

        # Crear tabla 'campaigns'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS campaigns (
                id SMALLINT PRIMARY KEY,
                customer_id SMALLINT,
                name VARCHAR(64),
                FOREIGN KEY (customer_id) REFERENCES customers(id)
            )
        """)
        print("Tabla 'campaigns' creada exitosamente.")

        # Crear tabla 'events'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                dt VARCHAR(19),
                campaign_id SMALLINT,
                status VARCHAR(64),
                FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
            )
        """)
        print("Tabla 'events' creada exitosamente.")

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
    Create_tables()