contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"\n✅ Contact '{name}' added successfully!\n")

def view_contacts():
    if contacts:
        print("\n----- Contact List -----")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")
    else:
        print("\nNo contacts available.\n")

def search_contact():
    search = input("Enter Name or Phone to Search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details["Phone"]:
            print(f"\nFound Contact:\nName: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            found = True
    if not found:
        print("\n❌ Contact not found.\n")

def update_contact():
    name = input("Enter the Name of the contact to update: ")
    if name in contacts:
        print("Leave blank if you don't want to update that field.")
        phone = input("New Phone (current: {}): ".format(contacts[name]["Phone"]))
        email = input("New Email (current: {}): ".format(contacts[name]["Email"]))
        address = input("New Address (current: {}): ".format(contacts[name]["Address"]))

        if phone: contacts[name]["Phone"] = phone
        if email: contacts[name]["Email"] = email
        if address: contacts[name]["Address"] = address
        print(f"\n✅ Contact '{name}' updated successfully!\n")
    else:
        print("\n❌ Contact not found.\n")

def delete_contact():
    name = input("Enter the Name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"\n🗑️ Contact '{name}' deleted successfully!\n")
    else:
        print("\n❌ Contact not found.\n")

def menu():
    while True:
        print("\n----- Contact Book -----")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

menu()
