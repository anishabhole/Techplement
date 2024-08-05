import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    else:
        # Pre-existing contacts
        return {
            "Alice Johnson": {"phone": "555-1234", "email": "alice@example.com"},
            "Bob Smith": {"phone": "555-5678", "email": "bob@example.com"}
        }

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print("Contact added successfully.")

def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        
        contacts[name] = {'phone': phone, 'email': email}
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
