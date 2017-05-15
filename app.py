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

    return cursor


def print_table(rows, descriptions):
    table = []
    column_names = [desc[0] for desc in descriptions]
    table.append(column_names)
    for row in rows:
        row = str(row).strip("()").split(", ")
        table.append(row)

    for row in table:
        print(", ".join(row))


def query_result(cursor, query):
    cursor.execute(query)
    rows = cursor.fetchall()

    return rows, cursor.description


def main():
    cursor = connect_database()
    rows, desc = query_result(cursor, """SELECT * FROM mentors;""")
    print_table(rows, desc)

if __name__ == '__main__':
    main()
