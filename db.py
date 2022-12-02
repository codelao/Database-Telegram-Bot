import sqlite3

class Database:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file, check_same_thread=False)
        self.cur = self.con.cursor()

    def add_number(self, number):
        with self.con:
            self.cur.execute("INSERT INTO numbers VALUES (?)", (number,))

    def get_number(self, number):
        with self.con:
            result = self.cur.execute("SELECT * FROM numbers WHERE number = ?", (number,)).fetchall()
            return bool(len(result)) #returns true or false
        
    def delete_number(self, number):
        with self.con:
            self.cur.execute("DELETE FROM numbers WHERE number = ?", (number,))
        
    def all_numbers(self):
        with self.con:
            listresult = self.cur.execute("SELECT * FROM numbers").fetchall()
            return len(listresult) #returns the number of all orders


