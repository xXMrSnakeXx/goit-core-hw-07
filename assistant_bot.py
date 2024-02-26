from handlers import *
from classes import *

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(update_contact(args, book))
        elif command == "remove":
            print(delete_contact(args, book))    
        elif command == "phone":
            for result in find_contact(args, book):
              print(result)
        elif command == "all":
            for result in get_all_contacts(book):
              print(result)
        elif command == "delete":
            print(delete_record(args, book)) 
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            for result in birthdays(book):
              print(result)
                              
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    
