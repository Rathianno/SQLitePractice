# Overview

Hello! I wrote this software as practice for SQLite3, it was really fun! I plan on doing more with this, but for now it's a showcase of some things it can do.


[Software Demo Video](https://youtu.be/6FsTEKfbHFI)

# Relational Database

I am using a single table, it has 4 rows, ID, First Name, Last Name, and Pay.

            create: Input employee into the database.
            print: Displays the employees on the database.
            reset: Cleans the database.
            budget: Returns the cost of all our employees.
            save: Sumbit new data into the database.
            quit: Closes the database.
            
# Development Environment

I ultilized the Sqlite3 Library on VSC, some extensions helped to read the .db files which helped in development, in its current state in 10/30/2021, it is using a temporary db stored in ram, connecting to ":memory:", this is to help out with some debugging for the time.

# Useful Websites

* [SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
* [SQLite Documentation](https://www.sqlite.org/docs.html)

# Future Work
* Make the print statements return the values only without formatting.
* Add more functions.
* Partition the commands into functions.
