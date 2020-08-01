import csv
import operator
import os.path


def order_data(filename="contacts.csv"):
    file = str(filename)

    with open(file, 'r') as data:
        reader = csv.reader(data)
        next(reader)
        sorted_data = sorted(reader, key=operator.itemgetter(0))

    contacts = {"Name": None, "Address": None, "Phone": None, "Email": None}
    with open(file, 'w') as data:
        writer = csv.DictWriter(data, fieldnames=contacts)
        writer.writeheader()
        writer = csv.writer(data)
        for line in sorted_data:
            writer.writerow(line)


def to_upper(name):
    name_list = list(name)
    name_list[0] = name_list[0].upper()
    for x in name_list:
        if x == ' ':
            index = name_list.index(x)
            name_list[index + 1] = name_list[index + 1].upper()
    return ''.join(name_list)


class ContactBook:

    def __init__(self, filename="contacts.csv"):
        self.contacts = {"Name": None, "Address": None, "Phone": None,
                         "Email": None}
        if not os.path.isfile(filename):
            with open(filename, 'w') as data_csv:
                writer = csv.DictWriter(data_csv, fieldnames=self.contacts)
                writer.writeheader()

    def add_contact(self, filename):

        data = ["Name", "Address", "Phone", "Email"]
        data_list = [None, None, None, None]
        for i in range(4):
            data_list[i] = input("Enter the {}: ".format(data[i]))
            if i == 0:
                data_list[0] = to_upper(str(data_list[0]))
        data_writer = csv.writer(filename)
        data_writer.writerow(data_list)

        return None

    def delete_contact(self, filename):
        contact = input("Which contact do you want to delete?: ")
        contact = to_upper(contact)
        with open(filename, 'r') as data_csv:
            data_reader = csv.reader(data_csv)
            data_aux = []
            for row in data_reader:
                data_aux.append(row)
        with open(filename, 'w') as data_csv:
            data_writer = csv.writer(data_csv)
            for row in data_aux:
                if row[0].lower() != contact.lower():
                    data_writer.writerow(row)
        return None

    def search_contact(self, filename):
        contact = input("Enter the contact to search: ")
        contact = to_upper(contact)
        data_reader = csv.reader(filename)
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
            print(
                "Contact Information for contact {}: ".format(contact_info[0]))
            for i in range(1, 4):
                print(
                    "{type}: {info}".format(type=data[i], info=contact_info[i]))

    def update_contact(self, filename):
        contact = input("Which contact do you want to update?: ")
        contact = to_upper(contact)
        data = ["Name", "Address", "Phone", "Email"]
        updated_data = [None, None, None, None]

        for i in range(4):
            aux = input("Enter the new {info}: ".format(info=data[i]))
            updated_data[i] = aux.lower()
        del data, aux

        with open(filename, 'r') as data_csv:
            data_reader = csv.reader(data_csv)
            data_aux = []
            for row in data_reader:
                data_aux.append(row)

        with open(filename, 'w') as data_csv:
            data_writer = csv.writer(data_csv)
            for row in data_aux:
                if row[0].lower() != contact.lower():
                    data_writer.writerow(row)
                else:
                    to_write = [None, None, None, None]
                    for i in range(len(updated_data)):
                        if updated_data[i] != '':
                            to_write[i] = updated_data[i]
                        else:
                            to_write[i] = row[i]
                    data_writer.writerow(to_write)
