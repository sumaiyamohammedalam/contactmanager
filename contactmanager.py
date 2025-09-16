class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None  # Points to next node


class ContactList:
    def __init__(self):
        self.head = None  # Start with empty list

    def add_contact(self, name, phone):
        new_node = Node(name, phone)
        if self.head is None:  # If list empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Go to the end
                current = current.next
            current.next = new_node
        print(f"✅ Contact {name} added successfully.")

    def display_contacts(self):
        if self.head is None:
            print("📭 Contact list is empty.")
            return
        current = self.head
        print("\n📒 Contact List:")
        while current:
            print(f"- {current.name}: {current.phone}")
            current = current.next

    def search_contact(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():  # case-insensitive match
                print(f"🔎 Found: {current.name}, Phone: {current.phone}")
                return
            current = current.next
        print("❌ Contact not found.")

    def delete_contact(self, name):
        current = self.head

        # If list empty
        if current is None:
            print("❌ Contact list is empty.")
            return

        # If head needs to be deleted
        if current.name.lower() == name.lower():
            self.head = current.next
            print(f"🗑️ Deleted {name}.")
            return

        prev = None
        while current and current.name.lower() != name.lower():
            prev = current
            current = current.next

        if current is None:
            print("❌ Contact not found.")
            return

        prev.next = current.next
        print(f"🗑️ Deleted {name}.")


# ----------------
# Main Menu Loop
# -----------------
contacts = ContactList()

while True:
    print("\n========= Contact Manager =========")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts.add_contact(name, phone)

    elif choice == "2":
        contacts.display_contacts()

    elif choice == "3":
        name = input("Enter name to search: ")
        contacts.search_contact(name)

    elif choice == "4":
        name = input("Enter name to delete: ")
        contacts.delete_contact(name)

    elif choice == "5":
        print("👋 Exiting Contact Manager. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
