from Objects import ContactBook
from sys import exit
import time


def is_csv(file_name):
    if not file_name.endswith(".csv"):
        file_name = file_name + ".csv"
    return file_name


def operations(book, file_name="contacts.csv"):
    dec = "y"
    while dec == "y" or dec == "Y":
        print(
            "What do you want to do?:\n(1) Add contact.\n(2) Update contact.\n"
            "(3) Delete contact.\n(4) Search contact.\n(5) Exit.\n"
            "Choose an answer: ")
        try:
            x = int(input())
        except ValueError:
            print("No operation found.")
            time.sleep(1)
            continue
        if x == 1:
            data_csv = open(file_name, "a")
            book.add_contact(data_csv)
        elif x == 2:
            book.update_contact(file_name)
        elif x == 3 or x == 4:
            if x == 3:
                book.delete_contact(file_name)
            else:
                data_csv = open(file_name, "r")
                book.search_contact(data_csv)
        elif x == 5:
            print("Closing...")
            exit()
        dec = input("Another operation? (Y/N): ")


def main():
    print("The default file name is 'contacts.csv'.\nDo you want to use a "
          "custom one? (Y/N): ")
    custom_file = input()

    if custom_file == "y" or custom_file == "Y":
        customfile_name = input("Enter the name of the csv file: ")
        file_name = is_csv(customfile_name)
        book = ContactBook(file_name)
        operations(book, file_name)
    else:
        book = ContactBook()
        operations(book)


if __name__ == "__main__":
    main()
