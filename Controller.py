import View
import Model
import time

STOP_TIME = 6

exitProgramm = False

while exitProgramm is False:
    View.hello()
    choice = input("Оберіть варіант: ")
    model = Model.db_model("videostreaming_service_database", "postgres", "Klopotanna20SQL", "")

    match choice:
        case "1":
            mas = model.get_table_names()
            View.show(mas)
            time.sleep(STOP_TIME)
        case "2":
            table = input("Введіть назву таблиці: ")
            mas = model.get_column_types(table)
            View.show(mas)
            time.sleep(STOP_TIME)
        case "3":
            table = input("Введіть назву таблиці: ")
            mas = model.get_column_names(table)
            View.show(mas)
            time.sleep(STOP_TIME)
        case "4":
            table = input("Введіть назву таблиці: ")
            mas = model.get_foreign_key_info(table)
            View.show(mas)
            time.sleep(STOP_TIME)
        case "5":
            table = input("Введіть назву таблиці: ")
            count = input("Введіть count: ")
            model.generate_data(table, count)
            mas = model.get_table_data(table)
            View.show(mas)
            time.sleep(STOP_TIME)
        case "6":
            table = input("Введіть назву таблиці: ")
            columns = input("Введіть назви колонок: ").split(' ')
            val = input("Введіть відповідні значення: ").split(' ')
            values = {key:value for (key,value) in zip(columns,val)}
            model.insert_data(table, values)
            print("result:\n")
            mas = model.get_table_data(table)
            View.show(mas)
            time.sleep(STOP_TIME)
        case "7":
            table = input("Введіть назву таблиці: ")
            columns = input("Введіть назви колонок: ").split(' ')
            val = input("Введіть відповідні значення: ").split(' ')
            values = {key:value for (key,value) in zip(columns,val)}
            model.change_data(table, values)
            mas = model.get_table_data(table)
            View.show(mas)
            time.sleep(STOP_TIME)
        case "8":
            table = input("Введіть назву таблиці: ")
            column = input("Назва колонки: ")
            param = input("Параметр: ")
            model.delete_data(table, column, param)
            mas = model.get_table_data(table)
            View.show(mas)
            time.sleep(STOP_TIME)
        case "9":
            table = input("Введіть назву таблиці: ")
            mas = model.get_table_data(table)
            View.show(mas)
            time.sleep(STOP_TIME)
        case "10":
            table = input("Введіть назву таблиці: ")
            mas = model.get_table_data(table)
            View.show(mas)
            time.sleep(STOP_TIME)

        case "0":
            exitProgramm = True

        case _:
            print("Error")
