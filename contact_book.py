import json

# Define the name of the file that will be used to store the contacts
CONTACTS_FILE = 'contacts.json'

def add_contact(name, email, phone):
    # Load the contacts from the file
    contacts = load_contacts()
    
    # Add the new contact to the list
    contacts.append({
        'name': name,
        'email': email,
        'phone': phone
    })
    
    # Save the updated contacts list to the file
    save_contacts(contacts)
    
def delete_contact(name):
    # Load the contacts from the file
    contacts = load_contacts()
    
    # Find the index of the contact with the specified name
    index = find_contact_index(contacts, name)
    
    if index is not None:
        # Remove the contact from the list
        del contacts[index]
        
        # Save the updated contacts list to the file
        save_contacts(contacts)
    
def edit_contact(name, email, phone):
    # Load the contacts from the file
    contacts = load_contacts()
    
    # Find the index of the contact with the specified name
    index = find_contact_index(contacts, name)
    
    if index is not None:
        # Update the contact's information
        contacts[index]['email'] = email
        contacts[index]['phone'] = phone
        
        # Save the updated contacts list to the file
        save_contacts(contacts)

def find_contact_index(contacts, name):
    # Find the index of the contact with the specified name
    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            return i
    return None

def load_contacts():
    try:
        # Try to open the contacts file and load its contents as JSON
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty list
        return []

def save_contacts(contacts):
    # Save the contacts list to the file as JSON
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f)

def render_contacts():
    # Load the contacts from the file
    contacts = load_contacts()
    
    # Generate an HTML table containing the contacts
    table = '<table>\n'
    table += '<tr><th>Name</th><th>Email</th><th>Phone</th><th>Action</th></tr>\n'
    for contact in contacts:
        table += f'<tr><td>{contact["name"]}</td><td>{contact["email"]}</td><td>{contact["phone"]}</td><td><a href="/edit/{contact["name"]}">Edit</a> | <a href="/delete/{contact["name"]}">Delete</a></td></tr>\n'
    table += '</table>\n'
    
    return table

