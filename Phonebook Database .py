# Phonebook.db Program
# Written By Wesley Greer on 5/1/2026

import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')

    cur = conn.cursor()

    create_entries_table(cur)

    add_entries(cur)
# create choices to allow for user input
    while True:
        print("\nPhonebook Menu")
        print("1. View all entries")
        print("2. Add new entry")
        print("3. Update entry")
        print("4. Delete entry")
        print("5. Exit")

        choice = input("Enter your choice: ")
# link each choice to a function
        if choice == '1':
            display_entries(cur)
        elif choice == '2':
            add_entry(cur)
        elif choice == '3':
            update_entry(cur)
        elif choice == '4':
            delete_entry(cur)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

        conn.commit()

    conn.close()

# create entries table if it doesn't already exist
def create_entries_table(cur):
    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (
                        EntryNumber INTEGER PRIMARY KEY,
                        Name TEXT,
                        PhoneNumber TEXT)''')

# add entries to entries table if it doesn't contain any information already
def add_entries(cur):
    cur.execute("SELECT COUNT(*) FROM Entries")
    if cur.fetchone()[0] == 0:
        data = [
            (1, 'John', '380-011-2000'),
            (2, 'Harry', '212-570-4168'),
            (3, 'Michele', '212-374-0778'),
            (4, 'Jordan', '122-106-6245'),
            (5,'Sally','234-456-4685'),
            (6, 'Emma', '122 - 099 - 8543'),
            (7,'Elizabeth','122-038-3994'),
            (8,'Mason', '122-023-7645'),
            (9,'Lily', '121-877-1769'),
            (10,'Bert','128-590-3220')]
        cur.executemany('''INSERT INTO Entries VALUES (?, ?, ?)''', data)


# define the functions for all of the choices
def display_entries(cur):
    print('Contents of phonebook.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]}')

def add_entry(cur):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    cur.execute('INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)',
                (name, phone))
    print("The entry has been added.")


def update_entry(cur):
    entry_id = input("Enter EntryNumber to update: ")
    name = input("Enter new name: ")
    phone = input("Enter new phone number: ")

    cur.execute('''UPDATE Entries
                   SET Name = ?, PhoneNumber = ?
                   WHERE EntryNumber = ?''',
                (name, phone, entry_id))

    if cur.rowcount == 0:
        print("The entry you are trying to update cannot be found.")
    else:
        print("The entry has been updated.")


def delete_entry(cur):
    entry_id = input("Enter EntryNumber to delete: ")

    cur.execute('DELETE FROM Entries WHERE EntryNumber = ?', (entry_id,))

    if cur.rowcount == 0:
        print("The entry you are trying to delete cannot be found.")
    else:
        print("the entry has been deleted.")


# Execute the main function.
if __name__ == '__main__':
    main()
