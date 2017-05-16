import psycopg2

MENU = 0
QUERY = 1


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


def menu_data():
    menu_dict = {1: ["The 2 name columns of the mentors table",
                     """SELECT first_name, last_name FROM mentors;"""],
                 2: ["The nick_names of all mentors working at Miskolc",
                     """SELECT nick_name FROM mentors
                        WHERE city = 'Miskolc';"""],
                 3: ["Full name and phone number of the girl named Carol",
                     """SELECT CONCAT(first_name,' ', last_name) as full_name, phone_number
                        FROM applicants
                        WHERE first_name = 'Carol';"""],
                 4: ["Who is the girl, who went to the famous Adipiscingenimmi University",
                     """SELECT CONCAT(first_name,' ', last_name) as full_name, phone_number
                        FROM applicants
                        WHERE email LIKE '%@adipiscingenimmi.edu';"""],
                 0: ["EXIT", ""]}
    return menu_dict


def print_menu():
    menu_dict = menu_data()
    print("\nQUERY MENU:\n")

    for i in range(len(menu_dict)):
        print("{} - {}".format(i, menu_dict[i][0]))


def choose_menu():
    menu_dict = menu_data()
    valid_answer = False

    while not valid_answer:
        try:
            answer = int(input("\nChoose from the menu: "))
            if answer:
                sql_query = menu_dict[answer][QUERY]
                return sql_query
            valid_answer = True
            return False
        except (ValueError, KeyError):
            print("\nInvalid entry. Try giving a number from the menu.")


def main():
    cursor = connect_database()
    end = False

    while not end:
        print_menu()
        query = choose_menu()
        if query:
            print_query(cursor, query)
        else:
            end = True


if __name__ == '__main__':
    main()
