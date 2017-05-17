import data_manager
import ui


def main():
    cursor = data_manager.connect_database()
    end = False

    while not end:
        ui.print_menu()
        query = ui.choose_menu()
        if query:
            ui.print_query_result(cursor, query)
        else:
            end = True


if __name__ == '__main__':
    main()
