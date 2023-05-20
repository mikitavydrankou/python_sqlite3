import sqlite3

connection = sqlite3.connect('database.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT
    )
''')

def add_record():
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    email = input('Enter email (optional): ')

    connection.execute('INSERT INTO records (name, age, email) VALUES (?, ?, ?)', (name, age, email))
    connection.commit()
    print('Record added successfully!')

def edit_record():
    record_id = int(input('Enter the ID of the record to edit: '))

    cursor = connection.execute('SELECT * FROM records WHERE id = ?', (record_id,))
    record = cursor.fetchone()

    if record:
        name = input('Enter new name: ')
        age = int(input('Enter new age: '))
        email = input('Enter new email (optional): ')

        connection.execute('UPDATE records SET name = ?, age = ?, email = ? WHERE id = ?', (name, age, email, record_id))
        connection.commit()
        print('Record updated successfully!')
    else:
        print('Record not found.')

def delete_record():
    record_id = int(input('Enter the ID of the record to delete: '))

    connection.execute('DELETE FROM records WHERE id = ?', (record_id,))
    connection.commit()
    print('Record deleted successfully!')

def view_records():
    cursor = connection.execute('SELECT * FROM records')
    records = cursor.fetchall()

    if records:
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Email: {record[3] if record[3] else 'N/A'}")
    else:
        print('No available records.')

while True:
    print('Menu:')
    print('1. Add a record')
    print('2. Edit a record')
    print('3. Delete a record')
    print('4. View records')
    print('0. Exit')

    choice = input('Choose an action: ')

    if choice == '1':
        add_record()
    elif choice == '2':
        edit_record()
    elif choice == '3':
        delete_record()
    elif choice == '4':
        view_records()
    elif choice == '0':
        break
    else:
        print('Invalid input. Please try again.')

connection.close()
