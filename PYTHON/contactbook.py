import tkinter as tk
from tkinter import messagebox

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management App")

        self.contacts = []
        
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, sticky="w")
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="w")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, sticky="w")
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=6, column=0, padx=10, pady=5)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=6, column=1, padx=10, pady=5)

        self.contacts_text = tk.Text(root, height=10, width=40)
        self.contacts_text.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            self.contacts.append(contact)
            self.clear_fields()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showwarning("Error", "Name and phone number are required fields.")

    def view_contacts(self):
        self.contacts_text.delete("1.0", tk.END)
        for contact in self.contacts:
            self.contacts_text.insert(tk.END, f"Name: {contact['name']}\n")
            self.contacts_text.insert(tk.END, f"Phone: {contact['phone']}\n")
            self.contacts_text.insert(tk.END, f"Email: {contact['email']}\n")
            self.contacts_text.insert(tk.END, f"Address: {contact['address']}\n")
            self.contacts_text.insert(tk.END, "-" * 30 + "\n")

    def search_contact(self):
        query = self.search_entry.get()
        matching_contacts = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
        self.contacts_text.delete("1.0", tk.END)
        for contact in matching_contacts:
            self.contacts_text.insert(tk.END, f"Name: {contact['name']}\n")
            self.contacts_text.insert(tk.END, f"Phone: {contact['phone']}\n")
            self.contacts_text.insert(tk.END, f"Email: {contact['email']}\n")
            self.contacts_text.insert(tk.END, f"Address: {contact['address']}\n")
            self.contacts_text.insert(tk.END, "-" * 30 + "\n")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
