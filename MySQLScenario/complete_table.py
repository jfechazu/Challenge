import mysql.connector
from mysql.connector import errorcode

def Complete_tables():
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

        # Completa la tabla customers
        cursor.execute("INSERT INTO customers (id, first_name, last_name) VALUES (1, 'Whitney', 'Ferrero')")
        cursor.execute("INSERT INTO customers (id, first_name, last_name) VALUES (2, 'Dickie', 'Romera')")
        cnx.commit()

        # Realizar una consulta
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        for customer in customers:
            print(customer)

        # Completa la tabla campaigns
        cursor.execute("INSERT INTO campaigns (id, customer_id, name) VALUES (1, 1, 'Upton Group')")
        cursor.execute("INSERT INTO campaigns (id, customer_id, name) VALUES (2, 1, 'Roob, Hudson and Rippin')")
        cursor.execute("INSERT INTO campaigns (id, customer_id, name) VALUES (3, 1, 'McCullough, Rempel and Larson')")
        cursor.execute("INSERT INTO campaigns (id, customer_id, name) VALUES (4, 1, 'Lang and Sons')")
        cursor.execute("INSERT INTO campaigns (id, customer_id, name) VALUES (5, 2, 'Ruecker, Hand and Haley')")
        cnx.commit()

        # Realizar una consulta
        cursor.execute("SELECT * FROM campaigns")
        campaigns = cursor.fetchall()
        for campaigns in campaigns:
            print(campaigns)

        # Completa la tabla events
        eventos = [
        ('2021-12-02 13:52:00', 1, 'failure'),
        ('2021-12-02 08:17:48', 2, 'failure'),
        ('2021-12-02 08:18:17', 2, 'failure'),
        ('2021-12-01 11:55:32', 3, 'failure'),
        ('2021-12-01 06:53:16', 4, 'failure'),
        ('2021-12-02 04:51:09', 4, 'failure'),
        ('2021-12-01 06:34:04', 5, 'failure'),
        ('2021-12-02 03:21:18', 5, 'failure'),
        ('2021-12-01 03:18:24', 5, 'failure'),
        ('2021-12-02 15:32:37', 1, 'success'),
        ('2021-12-01 04:23:20', 1, 'success'),
        ('2021-12-02 06:53:24', 1, 'success'),
        ('2021-12-02 08:01:02', 2, 'success'),
        ('2021-12-01 15:57:19', 2, 'success'),
        ('2021-12-02 16:14:34', 3, 'success'),
        ('2021-12-02 21:56:38', 3, 'success'),
        ('2021-12-01 05:54:43', 4, 'success'),
        ('2021-12-02 17:56:45', 4, 'success'),
        ('2021-12-02 11:56:50', 5, 'success'),
        ('2021-12-02 06:08:20', 5, 'success')
        ]
        query = """
        INSERT INTO events (dt, campaign_id, status)
        VALUES (%s, %s, %s)
        """
        cursor.executemany(query, eventos)
        cnx.commit()

        # Realizar una consulta
        cursor.execute("SELECT * FROM events")
        events = cursor.fetchall()
        for events in events:
            print(events)

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
    Complete_tables()