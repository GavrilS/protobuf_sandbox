'''
This script is using protobuf messages to read people's addresses from a file.

Usage:
python3 read_addresses.py 'ADDRESS_BOOK_FILE'
'''

import sys
import addressbook_pb2

# This function outputs the information in the address book in the console
def print_address_details(address_book):
    print('Printing the information from the address book...')
    for person in address_book.people:
        print('Name: ', person.name)
        print('ID: ', person.id)
        print('Email: ', person.email)
        print('Phones:')
        for phone in person.phones:
            print(' Type: ', phone.type)
            print(' Number: ', phone.number)
            print(' ---')

        print('-'*80)


# Main process: load the data in the provided address book and show it in the console
if len(sys.argv) != 2:
    print('Run the script with the following information: ', sys.argv[0], " 'ADDRESS_BOOK_FILE'")
    exit(1)

address_book = addressbook_pb2.AddressBook()

try:
    with open(sys.argv[1], 'rb') as f:
        address_book.ParseFromString(f.read())
except IOError:
    print('Could not open the file. Verify the file exists!')
    exit(1)

print_address_details(address_book)