import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def add(title, author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title, author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="", author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title,author,year,isbn)) 
    rows=cur.fetchall()  
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title="", author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title =?,author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close() 

connect()
#add("The EARTH","John Smith",1928,9153246)
#update(4,"The SUN","John Smith",1928,9153246)
#delete(3)
#print(search(author="John Smith"))
#print(view())