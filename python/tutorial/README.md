# Tutorial
The tutorial is going to build a very simple address book application that can read and write people's contact details to and from a file. Each person in the address book has a name, an ID, an email address, and a contact phone number.

# Steps

1. We will create our .proto file with the definitions of the messages our address book application will use. This is the file named addressbook.proto.

2. After the .proto definition file/s are created we will generate the classes we'll need to read and write AddressBook messages. To do this we need to run the protocol buffer compiler 'protoc' on our .proto file/s:

protoc --proto_path=./python/tutorial/ --python_out=./python/tutorial/ ./python/tutorial/addressbook.proto

* Notes:
    - we need to provide the path to our source directory(where our application code lives, the current directory is used by default), the destination directory(where we want the generated code to be put), and the path to our .proto file; the generated code will go into a file called addressbook_pb2.py with the above listed .proto file and the --python_out option
    - the option --python_out is used here, because we are using python in our app; similiar options exist for other languages