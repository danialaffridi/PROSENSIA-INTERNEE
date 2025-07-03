def is_valid_email(email):
    return "@" in email and "." in email

def manage_contact_book():
    contacts = {}

    while True:
        print("\n📘 Contact Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Retrieve Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter contact name: ").title()
            if name in contacts:
                print(f"⚠️ Contact '{name}' already exists.")
                continue

            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()

            if not is_valid_email(email):
                print("❌ Invalid email format. Must contain '@' and '.'")
                continue

            contacts[name] = {"phone": phone, "email": email}
            print(f"✅ Contact '{name}' added.")

        elif choice == "2":
            name = input("Enter contact name to update: ").title()
            if name not in contacts:
                print(f"❌ Contact '{name}' does not exist.")
                continue

            phone = input("Enter new phone number (leave blank to keep current): ").strip()
            email = input("Enter new email (leave blank to keep current): ").strip()

            if email and not is_valid_email(email):
                print("❌ Invalid email format. Update cancelled.")
                continue

            if phone:
                contacts[name]["phone"] = phone
            if email:
                contacts[name]["email"] = email

            print(f"🔄 Contact '{name}' updated.")

        elif choice == "3":
            name = input("Enter contact name to retrieve: ").title()
            if name in contacts:
                print(f"📇 {name} → Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
            else:
                print(f"❌ Contact '{name}' not found.")

        elif choice == "4":
            if not contacts:
                print("📭 Contact book is empty.")
            else:
                print("\n📖 All Contacts:")
                for name, info in contacts.items():
                    print(f"{name} → Phone: {info['phone']}, Email: {info['email']}")

        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a number between 1 and 5.")

# Run the contact book manager
manage_contact_book()
