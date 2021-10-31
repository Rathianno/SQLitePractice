import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()


def main():
    i = 'run'
    num = 1
    while i.lower() != 'shutdown':
        i = input(
            'Welcome to the Burgershop Database, what would you like to do?\n')
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

                #creation = str(creati)
                c.execute("""INSERT INTO employees(ID,FIRST,LAST,PAY) VALUES (?,?,?,?)""", beebo))

        if i == 'print':
            # for row in (c.execute("SELECT ID, first, last, pay from EMPLOYEES")):
            #     print("First Name = " + str(row[1]))
            #     print("Last Name = " + str(row[2]))
            #     print("Yearly Pay = " + str(row[3]))
            #     print("\n")
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

        if i == 'save':
            conn.commit()

        if i == 'quit':
            conn.close()
            break
        # else:
        #     main()


c.execute("""CREATE TABLE employees (
       ID real,
       FIRST text,
       LAST text,
        PAY    interger
       )""")


main()
conn.close()
