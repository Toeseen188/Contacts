
from flask import Flask, render_template, request

app = Flask(__name__)

contacts = {}  # an empty dictionary to store contacts

# function to add a new contact
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        contacts[name] = {"phone": phone, "email": email}
        message = f"{name} added to contacts."
        return render_template('add.html', message=message)
    else:
        return render_template('add.html')

# function to edit an existing contact
@app.route('/edit', methods=['GET', 'POST'])
def edit_contact():
    if request.method == 'POST':
        name = request.form['name']
        if name in contacts:
            phone = request.form['phone']
            email = request.form['email']
            if phone:
                contacts[name]["phone"] = phone
            if email:
                contacts[name]["email"] = email
            message = f"{name}'s contact information updated."
            return render_template('edit.html', message=message)
        else:
            message = f"{name} not found in contacts."
            return render_template('edit.html', message=message)
    else:
        return render_template('edit.html')

# function to delete a contact
@app.route('/delete', methods=['GET', 'POST'])
def delete_contact():
    if request.method == 'POST':
        name = request.form['name']
        if name in contacts:
            del contacts[name]
            message = f"{name} deleted from contacts."
            return render_template('delete.html', message=message)
        else:
            message = f"{name} not found in contacts."
            return render_template('delete.html', message=message)
    else:
        return render_template('delete.html')

# function to display all contacts
@app.route('/')
def display_contacts():
    if contacts:
        return render_template('index.html', contacts=contacts)
    else:
        message = "No contacts found."
        return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
