class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

    def search_contact(self, search_query):
        search_results = []
        for contact in self.contacts:
            if search_query in contact['name'] or search_query in contact['phone_number']:
                search_results.append(contact)
        return search_results

    def update_contact(self, index, name=None, phone_number=None, email=None, address=None):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            if name:
                contact['name'] = name
            if phone_number:
                contact['phone_number'] = phone_number
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Contact {deleted_contact['name']} deleted successfully!")
        else:
            print("Invalid contact index.")

contact_manager = ContactManager()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact_manager.add_contact(name, phone_number, email, address)

    elif choice == "2":
        print("All Contacts:")
        contact_manager.view_contacts()

    elif choice == "3":
        search_query = input("Enter name or phone number to search: ")
        search_results = contact_manager.search_contact(search_query)
        print("Search Results:")
        for contact in search_results:
            print(f"Name: {contact['name']}, Phone: {contact['phone_number']}")

    elif choice == "4":
        update_index = int(input("Enter the index of the contact you want to update: "))
        contact_manager.update_contact(update_index, email=input("Enter new email: "))

    elif choice == "5":
        delete_index = int(input("Enter the index of the contact you want to delete: "))
        contact_manager.delete_contact(delete_index)

    elif choice == "6":
        print("Exiting the Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
