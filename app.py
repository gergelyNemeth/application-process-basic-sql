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


def print_table(descriptions, rows):
    table = []
    column_names = [desc[0] for desc in descriptions]
    table.append(column_names)

    for row in rows:
        row = str(row).strip("()").split(", ")
        table.append(row)

    for row in table:
        print(", ".join(row))


def print_pretty_table(descriptions, rows):
    table = []
    column_names = [desc[0] for desc in descriptions]
    table.append(column_names)

    for row in rows:
        row = str(row).strip("()").replace("'", "").split(", ")
        table.append(row)

    column_lengths = [max([len(row[i]) for row in table]) for i in range(len(row))]
    separator_length = (sum(column_lengths) + len(column_lengths) * 3 + 1)
    separator = separator_length * "–"
    separator_menu = separator_length * "="

    for i, row in enumerate(table):
        row_pretty = []

        for j, column in enumerate(row):
            if column == "None":
                column = ""
            row_pretty.append("{0:<{width}}".format(str(column.strip(",")), width=column_lengths[j]))

        if i == 1:
            print(separator_menu)
        else:
            print(separator)
        print("| " + " | ".join(row_pretty) + " |")

    print(separator)


def query_result(cursor, query):
    cursor.execute(query)
    rows = cursor.fetchall()

    return cursor.description, rows


def print_query(cursor, query):
    desc, rows = query_result(cursor, query)
    print("\nQuery: \n{}".format(query))
    print_pretty_table(desc, rows)


def main():
    cursor = connect_database()

    print_query(cursor, """SELECT first_name, last_name FROM mentors;""")
    print_query(cursor, """SELECT nick_name FROM mentors WHERE city = 'Miskolc';""")
    print_query(cursor, """SELECT CONCAT(first_name,' ', last_name) as full_name, phone_number FROM applicants WHERE first_name = 'Carol';""")

if __name__ == '__main__':
    main()
