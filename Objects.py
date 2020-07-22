import csv
import operator
import os.path

def order_data(filename="contacts.csv"):
    file = str(filename)

    with open(file, "r") as data:
        reader = csv.reader(data, delimiter=",")
        sorted_data=sorted(reader, key=operator.itemgetter(0))
    with open(file, "w") as data:
        writer = csv.writer(data, delimiter=",")
        for line in sorted_data:
            writer.writerow(line)


class ContactBook:

    def __init__(self, filename="contacts.csv"):
        self.contacts = {"Name": None, "Address": None, "Phone": None,
                         "Email": None}
        if not os.path.isfile(filename):
            with open(filename, "w") as data_csv:
                writer = csv.DictWriter(data_csv, delimiter=",",
                                        fieldnames=self.contacts)
                writer.writeheader()

    def add_contact(self, filename):

        data = ["Name", "Address", "Phone", "Email"]
        data_list = [None, None, None, None]
        for i in range(4):
            data_list[i] = input("Enter the {}: ".format(data[i]))
        data_writer = csv.writer(filename, delimiter=",")
        data_writer.writerow(data_list)

        return None

    def delete_contact(self, filename):
        contact = input("Which contact do you want to delete?: ")
        with open(filename, "r") as data_csv:
            data_reader = csv.reader(data_csv, delimiter=",")
            data_aux = []
            for row in data_reader:
                data_aux.append(row)
        with open(filename, "w") as data_csv:
            data_writer = csv.writer(data_csv, delimiter=",")
            for row in data_aux:
                if row[0].lower() != contact.lower():
                    data_writer.writerow(row)
        return None

    def search_contact(self, filename):
        contact = input("Enter the contact to search: ")
        data_reader = csv.reader(filename, delimiter=",")
        contact_info = []
        data = ["Name", "Address", "Phone", "Email"]
        count = 0
        for row in data_reader:
            if row[0].lower() == contact.lower():
                contact_info = list(row)
                count += 1
        if count == 0:
            print("No contact found with than name.")
        else:
            print("Contact Information for contact {}: ".format(contact_info[0]))
            for i in range(1, 4):
                print("{type}: {info}".format(type=data[i], info=contact_info[i]))

    def update_contact(self, filename):
        contact = input("Which contact do you want to update?: ")
        data = ["Name", "Address", "Phone", "Email"]
        updated_data = [None, None, None, None]

        for i in range(4):
            data_aux = input("Enter the new {info}: ".format(info=data[i]))
            updated_data[i] = data_aux
        with open(filename, "r") as data_csv:
            data_reader = csv.reader(data_csv, delimiter=",")
            data_aux = []
            for row in data_reader:
                data_aux.append(row)
        with open(filename, "w") as data_csv:
            data_writer = csv.writer(data_csv, delimiter=",")
            for row in data_aux:
                if row[0].lower() != contact.lower():
                    data_writer.writerow(row)
                else:
                    data_writer.writerow(updated_data)
