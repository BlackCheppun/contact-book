import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS contacts 
        (id INTEGER PRIMARY KEY,firstname text, lastname text, emailadress text, phonenumber text
         )""")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM contacts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, firstname, lastname, emailadress, phonenumber):
        self.cur.execute("INSERT INTO contacts VALUES(NULL, ?, ?, ?, ?)",
                         (firstname, lastname, emailadress, phonenumber))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM contacts WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, firstname, lastname, emailadress, phonenumber):
        self.cur.execute("UPDATE contacts SET firstname = ?, lastname = ?, emailadress = ?, phonenumber = ? WHERE id =? ",
                         (firstname, lastname, emailadress, phonenumber, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
#to intialisze it we create an object of Databese we give a string with the name on it such as 'contacts.db'
# db = Database('contacts.db')

