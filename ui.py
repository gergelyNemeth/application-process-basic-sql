import data_manager

MENU = 0
QUERY = 1


def menu_data():
    menu_dict = {0: ["EXIT", ""],
                 1: ["The two name columns of the mentors table",
                     """SELECT first_name, last_name FROM mentors ORDER BY id;"""],
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
                 5: ["Add Marcus Schaffarzyk to the applicants",
                     """INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                        VALUES('Marcus', 'Schaffarzyk',
                            '003620/725-266', 'djnovus@groovecoverage.com', 54823);
                        SELECT * from applicants WHERE application_code = 54823;"""],
                 6: ["Change Jemima Foreman's phone number to 003670/223-7459",
                     """UPDATE applicants SET phone_number = '003670/223-7459'
                        WHERE first_name = 'Jemima' AND last_name = 'Foreman';
                        SELECT * FROM applicants WHERE phone_number = '003670/223-7459';"""],
                 7: ["Delete Arsenio and his friend (with email @mauriseu.net)",
                     """DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';
                        SELECT * FROM applicants WHERE email LIKE '%@mauriseu.net';"""]
                 }
    return menu_dict


def print_menu():
    menu_dict = menu_data()
    print("\nAPPLICATION PROCESS")
    print("\nQUERY MENU:\n")

    for i in range(len(menu_dict)):
        print("{} - {}".format(i, menu_dict[i][MENU]))


def choose_menu():
    menu_dict = menu_data()
    valid_answer = False

    while not valid_answer:
        try:
            answer = int(input("\nChoose from the menu: "))
            if answer:
                sql_query = menu_dict[answer][QUERY].replace("  ", "")
                return sql_query
            valid_answer = True
            return False
        except (ValueError, KeyError):
            print("\nInvalid entry. Enter a number from the menu.")


def print_table(descriptions, rows):
    table = []
    column_names = [description[0] for description in descriptions]
    table.append(column_names)

    for row in rows:
        row = str(row).strip("()").split(", ")
        table.append(row)

    for row in table:
        print(", ".join(row))


def print_pretty_table(descriptions, rows):
    table = []
    column_names = [description[0] for description in descriptions]
    table.append(column_names)

    for row in rows:
        row = str(row).strip("()").replace("'", "").split(", ")
        table.append(row)

    column_lengths = [max([len(row[i]) for row in table]) for i in range(len(row))]
    separator_length = (sum(column_lengths) + len(column_lengths) * 3 + 1)
    separator = separator_length * "–"

    for i, row in enumerate(table):
        row_pretty = []

        for j, column in enumerate(row):
            if column == "None":
                column = ""
            row_pretty.append("{0:<{width}}".format(str(column.strip(",")), width=column_lengths[j]))

        if i < 2:
            print(separator)

        print("| " + " | ".join(row_pretty) + " |")

    print(separator)


def print_query_result(cursor, query):
    print("\nSQL query: \n{}\n".format(query))
    try:
        descriptions, rows = data_manager.query_result(cursor, query)
        print_pretty_table(descriptions, rows)
    except Exception as e:
        print("No query result to print")
