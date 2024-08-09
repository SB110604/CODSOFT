import json

def load_contacts(filename='contacts.json'):
    """Load contacts from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts, filename='contacts.json'):
    """Save contacts to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact for {name} added.")

def view_contacts(contacts):
    """Display all contacts."""
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")

def search_contact(contacts):
    """Search for a contact by name or phone number."""
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    if not found:
        print("No contact found.")

def update_contact(contacts):
    """Update a contact's details."""
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"\nCurrent details for {name}:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")

        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address

        print(f"Contact for {name} updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted.")
    else:
        print("Contact not found.")

def main():
    """Main function to run the Contact Book application."""
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the Contact Book application
if __name__ == "__main__":
    main()
