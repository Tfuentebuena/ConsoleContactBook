import os
import csv_worker
import sql_up
from sys import exit
from time import sleep


def is_csv(file_name):
    if not file_name.endswith(".csv"):
        file_name = file_name + ".csv"
    return file_name


def operations(book, choices, file_name="contacts.csv"):
    dec = 'y'

    while dec == 'y' or dec == 'Y':
        print(
            "What do you want to do?:\n(1) Add contact.\n(2) Update contact.\n"
            "(3) Delete contact.\n(4) Search contact.\n(5) Exit.\n"
            "Choose an answer: ")
        try:
            x = int(input())
        except ValueError:
            print("No operation found.")
            sleep(1)
            continue
        if x == 1:
            data_csv = open(file_name, 'a')
            book.add_contact(data_csv)
            choices.append(x)
        elif x == 2:
            book.update_contact(file_name)
            choices.append(x)
        elif x == 3:
            book.delete_contact(file_name)
            choices.append(x)
        elif x == 4:
            data_csv = open(file_name, 'r')
            book.search_contact(data_csv)
            choices.append(x)
        elif x == 5:
            print("Closing...")
            exit()
        dec = input("Another operation? (Y/N): ")


def main():
    print("The default file name is 'contacts.csv'.\nDo you want to use a "
          "custom one? (Y/N): ")
    custom_file = input()
    choices = []

    if custom_file == 'y' or custom_file == 'Y':
        customfile_name = input("Enter the name of the csv file: ")
        file_name = is_csv(customfile_name)
        book = csv_worker.ContactBook(file_name)
        operations(book, choices, file_name)
        if 1 in choices or 2 in choices:
            csv_worker.order_data(file_name)
        if os.path.isfile("sql_DB.db"):
            os.remove("sql_DB.db")
            sql_up.uploader(file_name)
        else:
            sql_up.uploader(file_name)

    else:
        book = csv_worker.ContactBook()
        operations(book, choices)
        csv_worker.order_data()
        if 1 in choices or 2 in choices:
            csv_worker.order_data()

        if os.path.isfile("sql_DB.db"):
            os.remove("sql_DB.db")
            sql_up.uploader()
        else:
            sql_up.uploader()


if __name__ == "__main__":
    main()
