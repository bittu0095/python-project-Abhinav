# CONTACT MANAGEMENT SYSTEM
# A simple Python 3 project using CRUD operations

contacts = []


def is_valid_phone(phone):
    """Return True only if the phone has exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10


def phone_exists(phone, ignore_index=None):
    """Check whether a phone number is already saved."""
    for index, contact in enumerate(contacts):
        if index != ignore_index and contact["phone"] == phone:
            return True
    return False


def add_contact():
    print("\n--- ADD CONTACT ---")
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter 10-digit phone number: ").strip()
    if not is_valid_phone(phone):
        print("Enter exactly 10 digits.")
        return
    if phone_exists(phone):
        print("Contact with this number already exists.")
        return

    email = input("Enter email address: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print("Contact added successfully.")


def view_contacts():
    print("\n--- ALL CONTACTS ---")
    if not contacts:
        print("No contacts saved.")
        return

    for number, contact in enumerate(contacts, start=1):
        print(f"\nContact {number}")
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


def search_contact():
    print("\n--- SEARCH CONTACT ---")
    search_name = input("Enter name to search: ").strip().lower()
    found = False

    for contact in contacts:
        if search_name in contact["name"].lower():
            print("\nContact found:")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    print("\n--- UPDATE CONTACT ---")
    phone = input("Enter the phone number of the contact to update: ").strip()

    for index, contact in enumerate(contacts):
        if contact["phone"] == phone:
            print("Leave a field blank to keep its current value.")

            new_name = input(f"New name [{contact['name']}]: ").strip()
            new_phone = input(f"New phone [{contact['phone']}]: ").strip()
            new_email = input(f"New email [{contact['email']}]: ").strip()

            if new_phone:
                if not is_valid_phone(new_phone):
                    print("Enter exactly 10 digits. Update cancelled.")
                    return
                if phone_exists(new_phone, ignore_index=index):
                    print("Contact with this number already exists. Update cancelled.")
                    return
                contact["phone"] = new_phone

            if new_name:
                contact["name"] = new_name
            if new_email:
                contact["email"] = new_email

            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact():
    print("\n--- DELETE CONTACT ---")
    phone = input("Enter the phone number of the contact to delete: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            print("Total contacts:", len(contacts))
            return

    print("Contact not found.")


def main():
    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

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
            print("Thank you for using Contact Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
