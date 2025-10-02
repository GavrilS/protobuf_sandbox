'''
This script is using protobuf messages to write messages to a file.

Usage:
python3 write_addresses.py 'ADDRESS_BOOK_FILE'
'''

import  sys
import addressbook_pb2


# Method to get data for a new person to be added from user input
def create_new_address(person):
    person.name = input('Provide a name for the new person: ')
    person.id = int(input('Provide an ID for the new person: '))
    person.email = input('Provide an email for the new person(leave empty to skip): ')

    while True:
        number = input('Provide a number for the new person(leave empty to skip adding more numbers): ')

        if not number:
            break

        phone_number = person.phones.add()
        phone_number.number = number

        phone_type = input('Is this a mobile, home or work number?: ')
        if phone_type.lower() == 'mobile':
            phone_number.type = addressbook_pb2.Person.PhoneType.PHONE_TYPE_MOBILE
        elif phone_type.lower() == 'home':
            phone_number.type = addressbook_pb2.Person.PhoneType.PHONE_TYPE_HOME
        elif phone_type.lower() == 'work':
            phone_number.type = addressbook_pb2.Person.PhoneType.PHONE_TYPE_WORK
        else:
            print('No type specified, leaving as default.')


# Main procedure: read the entire content of a address book, add a new person based on user input and save the content again

if len(sys.argv) != 2:
    print('The usage of the script is: ', sys.argv[0], "'ADDRESS_BOOK_FILE'")
    sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

try:
    with open(sys.argv[1], 'rb') as f:
        address_book.ParseFromString(f.read())
except IOError:
    print('Error opening file: ', sys.argv[1], ' Creating a new one.')


create_new_address(address_book.people.add())

with open(sys.argv[1], 'wb') as f:
    f.write(address_book.SerializeToString())