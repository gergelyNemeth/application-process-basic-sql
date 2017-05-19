import data_manager
import ui


def main():
    end = False

    while not end:
        ui.print_menu()
        query = ui.choose_menu()
        if query:
            ui.print_query_result(query)
        else:
            end = True


if __name__ == '__main__':
    main()
