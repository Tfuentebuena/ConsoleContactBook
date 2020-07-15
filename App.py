from Objects import ContactBook
from sys import exit
import time


def operations(book):
    dec = "y"
    while dec == "y" or dec == "Y":
        print("What do you want to do?:\n(1) Add contact.\n(2) Update contact.\n"
              "(3) Delete contact.\n(4) Search contact.\n(5) Exit.\n"
              "Choose an answer: ")
        x = int(input())
        if type(x) != int or x > 5 or x < 1:
            print("No operation found.")
            time.sleep(1)
            continue
        if x == 1:
            data_csv = open("contacts.csv", "a")
            book.add_contact(data_csv)
        elif x == 2:
            book.update_contact()
        elif x == 3 or x == 4:
            if x == 3:
                book.delete_contact()
            else:
                data_csv = open("contacts.csv", "r")
                book.search_contact(data_csv)
        elif x == 5:
            print("Closing...")
            exit()
        dec = input("Another operation? (Y/N): ")


def main():
    book = ContactBook()
    operations(book)


if __name__=="__main__":
    main()
