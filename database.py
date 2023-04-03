import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db, check_same_thread=False)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, height INTEGER)")

    def insert(self,email,height):
        #checking if email already exists in db
        self.cur.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,))
        rows = self.cur.fetchall()
        #print(type(rows)) #type of the row variable is list
        exist_variable = rows[0][0] #extracting existing email count value from the list, [(1,)] -> 1
        #print(exist_variable)
        #adding email if not exists or skipping this task if email is there
        if(exist_variable == 0):
            self.cur.execute("INSERT INTO users VALUES (NULL,?,?)", (email,height))
            self.conn.commit()
        else:
            print("Email already exists!")
        return exist_variable

    #method to calculate average height of all users + users count
    def average(self):
        self.cur.execute("SELECT AVG(height) FROM users ")
        avg_height_rawdata = self.cur.fetchall()
        avg_height = round(avg_height_rawdata[0][0])
        self.cur.execute("SELECT COUNT(height) FROM users ")
        users_count_rawdata = self.cur.fetchall()
        users_count = users_count_rawdata[0][0]
        #print(avg_height, users_count)
        return(avg_height, users_count)

    def __del__(self):
        self.conn.close()

