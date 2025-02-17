def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Not found, try another one."
        except IndexError:
            return "Not found, try another one."
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_username_phone(args, contacts):
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact changed."

@input_error
def phone_username(args, contacts):
        name = args[0]
        return contacts.get(name, "Contact not found.")

def all(contacts):
    return contacts

def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()