from flask import Flask, request, render_template, redirect, url_for
import contact_book

app = Flask(__name__)

@app.route('/')
def index():
    # Render the contacts as an HTML table
   
    contacts_table = contact_book.render_contacts()
    return render_template('index.html', contacts_table=contacts_table)

@app.route('/add', methods=['POST'])
def add():
    # Get the contact information from the form data
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    
    # Add the new contact
    contact_book.add_contact(name, email, phone)
    
    # Redirect back to the index page
    return redirect(url_for('index'))

@app.route('/delete/<name>')
def delete(name):
    # Delete the contact with the specified name
    contact_book.delete_contact(name)
    
    # Redirect back to the index page
    return redirect(url_for('index'))

@app.route('/edit/<name>', methods=['GET', 'POST'])
def edit(name):
    # Load the contact's information
    contacts = contact_book.load_contacts()
    index = contact_book.find_contact_index(contacts, name)
    if index is None:
        # If the contact doesn't exist, redirect back to the index page
        return redirect(url_for('index'))
    contact = contacts[index]
    
    if request.method == 'POST':
        # Update the contact's information
        email = request.form['email']
        phone = request.form['phone']
        contact_book.edit_contact(name, email, phone)
        
        # Redirect back to the index page
        return redirect(url_for('index'))
    else:
        # Render the edit contact page
        return render_template('edit.html', name=name, email=contact['email'], phone=contact['phone'])

if __name__ == '__main__':
    app.run()

