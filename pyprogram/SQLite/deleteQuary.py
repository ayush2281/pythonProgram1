import sqlite3

conn = sqlite3.connect("sqlite.db")
st_name=input("Enter the student id:-")
conn.execute("DELETE FROM student where st_name="+st_name)
conn.commit()
conn.close()