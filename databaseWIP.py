import sqlite3

# Executes the code to the library.db database file
conn = sqlite3.connect('library.db')
# Creates cursor object
cursor = conn.cursor()

# Creates admin table in the db for login
cursor.execute('''CREATE TABLE IF NOT EXISTS admin(
            admin_user TEXT PRIMARY KEY NOT NULL,
            admin_password TEXT NOT NULL
            )''')
# Creates the book table in the db
cursor.execute('''CREATE TABLE IF NOT EXISTS book(
            book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            book_title TEXT NOT NULL,
            book_author TEXT NOT NULL,
            book_genre TEXT NOT NULL,
            book_availability TEXT NOT NULL,
            isbn TEXT NOT NULL
            )''')
# Creates the member table in the db
cursor.execute('''CREATE TABLE IF NOT EXISTS member(
            member_id INTEGER PRIMARY UNIQUE NOT NULL,
            member_name TEXT NOT NULL,
            member_email TEXT NOT NULL,
            member_number INTEGER NOT NULL,
            member_address TEXT NOT NULL,
            borrow_history TEXT
            )''')
# Creates the transactions table in the db, funny enough I ran into an error because it was 'transaction'
# Still don't know why it caused an error without the s
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions(
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            borrow_date TEXT,
            return_date TEXT,
            due_date TEXT,
            book_id INTEGER,
            member_id INTEGER,
            FOREIGN KEY(book_id) REFERENCES book(book_id),
            FOREIGN KEY(member_id) REFERENCES member(member_id)
            )''')


# Forces into admin table values for admin user and password so we have admin login pre-made
# Videos were telling me the (?, ?) after VALUES helps to protect against SQL injection attacks
conn.execute('INSERT INTO admin (admin_user, admin_password) VALUES(?, ?)', ('admin', 'password'))

# Commits then closes 
conn.commit()
cursor.close()
conn.close()