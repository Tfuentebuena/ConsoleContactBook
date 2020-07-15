import csv
import os.path


class ContactBook:

    def __init__(self):
        self.contacts = {"Name": None, "Address": None, "Phone": None,
                         "Email": None}
        if not os.path.isfile("contacts.csv"):
            with open("contacts.csv", "w") as data_csv:
                writer = csv.DictWriter(data_csv, delimiter=",",
                                        fieldnames=self.contacts)
                writer.writeheader()

    def add_contact(self, data_csv):
        data = ["Name", "Address", "Phone", "Email"]
        data_list = [None, None, None, None]
        for i in range(4):
            data_list[i] = input("Enter the {}: ".format(data[i]))
        data_writer = csv.writer(data_csv, delimiter=",")
        data_writer.writerow(data_list)
        return None

    def delete_contact(self):
        contact = input("Which contact do you want to delete?: ")
        with open("contacts.csv", "r") as data_csv:
            data_reader = csv.reader(data_csv, delimiter=",")
            data_aux = []
            for row in data_reader:
                data_aux.append(row)
        with open("contacts.csv", "w") as data_csv:
            data_writer = csv.writer(data_csv, delimiter=",")
            for row in data_aux:
                if row[0].lower() != contact.lower():
                    data_writer.writerow(row)
        return None

    def search_contact(self, data_csv):
        contact = input("Enter the contact to search: ")
        data_reader = csv.reader(data_csv, delimiter=",")
        contact_info = []
        data = ["Name", "Address", "Phone", "Email"]
        for row in data_reader:
            if row[0].lower() == contact.lower():
                contact_info = list(row)
        print("Contact Information for contact {}: ".format(contact_info[0]))
        for i in range(1, 4):
            print("{type}: {info}".format(type=data[i], info=contact_info[i]))

    def update_contact(self):
        contact = input("Which contact do you want to update?: ")
        data = ["Name", "Address", "Phone", "Email"]
        updated_data = [None, None, None, None]

        for i in range(4):
            data_aux = input("Enter the new {info}: ".format(info=data[i]))
            updated_data[i] = data_aux
        with open("contacts.csv", "r") as data_csv:
            data_reader = csv.reader(data_csv, delimiter=",")
            data_aux = []
            for row in data_reader:
                data_aux.append(row)
        with open("contacts.csv", "w") as data_csv:
            data_writer = csv.writer(data_csv, delimiter=",")
            for row in data_aux:
                if row[0].lower() != contact.lower():
                    data_writer.writerow(row)
                else:
                    data_writer.writerow(updated_data)
