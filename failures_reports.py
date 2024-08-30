import mysql.connector
from mysql.connector import errorcode

def get_customers_with_failures():
    try:
        # Conexión a la base de datos MySQL
        cnx = mysql.connector.connect(
            host='hostname',
            user='username',  # Reemplaza con tu usuario de MySQL
            password='password',  # Reemplaza con tu contraseña de MySQL
            database='database'  # Reemplaza con el nombre de tu base de datos
        )
        cursor = cnx.cursor()

        # Consulta SQL para obtener los clientes con más de 3 eventos de "failure"
        query = """
        SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer, COUNT(e.status) AS failures
        FROM customers c
        JOIN campaigns ca ON c.id = ca.customer_id
        JOIN events e ON ca.id = e.campaign_id
        WHERE e.status = 'failure'
        GROUP BY c.id
        HAVING COUNT(e.status) > 3
        """

        cursor.execute(query)

        # Mostrar resultados
        results = cursor.fetchall()
        for (customer, failures) in results:
            print(f"{customer}, {failures}")

    except mysql.connector.Error as err:
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

if __name__ == "__main__":
    get_customers_with_failures()
