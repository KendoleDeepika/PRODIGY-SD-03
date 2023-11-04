# Initialize an empty dictionary to store contacts
contacts = {}

def add_contact():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = {"Phone": phone_number, "Email": email}
    print(f"Contact for {name} has been added.")

def view_contacts():
    print("Contacts:")
    for name, contact_info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {contact_info['Phone']}")
        print(f"Email: {contact_info['Email']}")
        print()

def edit_contact():
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        print(f"Editing contact for {name}:")
        phone_number = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        contacts[name] = {"Phone": phone_number, "Email": email}
        print(f"Contact for {name} has been updated.")
    else:
        print(f"Contact for {name} not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} has been deleted.")
    else:
        print(f"Contact for {name} not found.")

while True:
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")
