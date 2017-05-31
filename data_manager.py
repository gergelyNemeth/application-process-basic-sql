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
        columns = [description[0] for description in cursor.description]
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()

    return columns, rows


def query_mentors():
    query = """SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS name, schools.name AS school, schools.country
               FROM mentors
               INNER JOIN schools ON mentors.city = schools.city
               ORDER BY mentors.id
               ;"""
    columns, rows = query_result(query)

    return columns, rows


def query_all_school():
    query = """SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS name, schools.name AS school, schools.country
               FROM mentors
               RIGHT JOIN schools ON mentors.city = schools.city
               ORDER BY mentors.id
               ;"""
    columns, rows = query_result(query)

    return columns, rows


def query_mentors_by_country():
    query = """SELECT schools.country, COUNT(mentors.id)
               FROM mentors
               RIGHT JOIN schools ON mentors.city = schools.city
               GROUP BY schools.country
               ORDER BY schools.country
               ;"""
    columns, rows = query_result(query)

    return columns, rows


def query_contacts():
    query = """SELECT schools.name AS school,
                      CONCAT(mentors.first_name, ' ', mentors.last_name) AS contact_name,
                      mentors.email
               FROM mentors
               INNER JOIN schools ON mentors.city = schools.city
               WHERE mentors.id = schools.contact_person
               ORDER BY schools.name
               ;"""
    columns, rows = query_result(query)

    return columns, rows
