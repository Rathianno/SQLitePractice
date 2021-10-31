import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()


def main():
    i = 'run'
    num = 1
    while i.lower() != 'shutdown':
        i = 'run'
        i = input(
            'Welcome to the Burgershop Database, what would you like to do?\n').lower()
        if i == 'create':
            numb = input('Enter employee ID : ')
            if numb.isdecimal() == False:
                print('Invalid input.')
                main()

            fname = input('Enter the employee\'s first name : ')
            lname = input('Enter the employee\'s last name : ')
            ypay = input('Enter the employee\'s yearly pay : ')
            beebo = [numb, fname, lname, ypay]
            creati = (


                c.execute("""INSERT INTO employees(ID,FIRST,LAST,PAY) VALUES (?,?,?,?)""", beebo))

        if i == 'print':
            c.execute("SELECT * FROM employees")
            print(c.fetchall())

        if i == 'reset':
            print(str(c.execute("SELECT COUNT(ID)FROM Employees")))
            d = input('Are you sure? y/n \n')
            if d.lower() == 'y':
                c.execute("DELETE FROM employees")
                print('Deleted.')
            else:
                main()
        if i == 'budget':
            c.execute("""SELECT SUM(pay) AS budget FROM employees""")
            print(c.fetchall())

        if i == 'save':
            conn.commit()

        if i == 'help':
            print("""
            create: Input employee into the database.\n
            print: Displays the employees on the database.\n 
            reset: Cleans the database.\n
            budget: Returns the cost of all our employees.\n
            save: Sumbit new data into the database.\n
            quit: Closes the database.\n
            """)

        if i == 'quit':
            conn.close()
            break
        else:
            main()


c.execute("""CREATE TABLE employees (
       ID real,
       FIRST text,
       LAST text,
        PAY    interger
       )""")


main()
conn.close()
