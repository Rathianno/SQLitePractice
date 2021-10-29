import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

i= 'run'
num = 1
while i.lower() != 'quit':
    def run():
        i = input('Welcome to the Burgershop Database, what would you like to do?\n')
        if i == 'create':
            id = input('Enter employee ID : ')
            if id.isdecimal() == False:
                print('Invalid input.')

            first = input('Enter the employee\'s first name : ')
            last = input('Enter the employee\'s first name : ')
            pay = input('Enter the employee\'s yearly pay : ')

        c.execute("INSERT INTO employees VALUES(?,?,?,?)",(id,first,last,pay))

       # c.execute("INSERT INTO employees VALUES(,?,?,?", num,(input("F?irst name:")),(input("Last name:")), (input("Yearly salary:")))

    if i == 'print':
            for row in (c.execute("SELECT id, first, last, pay from EMPLOYEES")):
                print( "First Name = " + str(row[1]))
                print( "Last Name = " + str(row[2]))
                print( "Yearly Pay = " + str(row[3]))
                print( "\n")

#c.execute("""CREATE TABLE employees (
#        ID real,
#        first text,
#        last text,
#         pay interger
#        )""")

conn.commit()

conn.close()