import psycopg2


def connect_database():
    try:
        # setup connection string
        connect_str = "dbname='gergo' user='gergo' host='localhost'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

    return cursor, conn


def query_result(query):
    try:
        cursor, conn = connect_database()
        cursor.execute(query)
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()

    return cursor.description, rows