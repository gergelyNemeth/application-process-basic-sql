import psycopg2


def print_table(rows):
    for row in rows:
        row = str(row).strip("()").split(", ")
        for i, column in enumerate(row):
            if i < len(row) - 1:
                print(column, end=', ')
            else:
                print(column)


def main():
    try:
        # setup connection string
        connect_str = "dbname='gergo' user='gergo' host='localhost' password='Jn3.16'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # removing the test table if it already exists
        cursor.execute("""SELECT * FROM mentors;""")
        # Fetch and print the result of the last execution
        rows = cursor.fetchall()
        print_table(rows)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

if __name__ == '__main__':
    main()
