from tkinter import *
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="")
cur = con.cursor(buffered=True)

# Create / Use database
try:
    cur.execute("USE registration")
except:
    cur.execute("CREATE DATABASE registration")
    cur.execute("USE registration")

# Create table if not exists
try:
    cur.execute("DESCRIBE persons")
except:
    cur.execute("""
        CREATE TABLE persons(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(20),
            age INT,
            gender VARCHAR(10),
            email VARCHAR(30),
            mobile VARCHAR(11)
        )
    """)

# ------------------ FUNCTION ------------------

def registration():
    name = e1.get()
    age = e2.get()
    gender = e3.get()
    email = e4.get()
    mobile = e5.get()
    
    cur.execute(
        "INSERT INTO persons(name, age, gender, email, mobile) VALUES (%s, %s, %s, %s, %s)",
        (name, age, gender, email, mobile)
    )
    con.commit()
    print("Data inserted successfully!")

# ----------------- GUI -----------------------

root = Tk()
root.geometry("500x500")
root.title("Registration form")

Label(root, text="Personal details").grid(row=1, column=1)

Label(root, text="Name").grid(row=2, column=1)
Label(root, text="Age").grid(row=3, column=1)
Label(root, text="Gender").grid(row=4, column=1)
Label(root, text="Email").grid(row=5, column=1)
Label(root, text="Mobile No.").grid(row=6, column=1)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)

e1.grid(row=2, column=2)
e2.grid(row=3, column=2)
e3.grid(row=4, column=2)
e4.grid(row=5, column=2)
e5.grid(row=6, column=2)

Button(root, text="Submit here", command=registration).grid(row=7, column=2)

root.mainloop()
