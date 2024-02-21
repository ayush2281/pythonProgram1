import sqlite3
conn = sqlite3.connect("sqlite.db")

conn.execute('''
   update student set st_name='piyush' where st_name=1




    ''')
conn.commit()
conn.close()