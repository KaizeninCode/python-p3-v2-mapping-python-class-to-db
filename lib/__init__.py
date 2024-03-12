# lib/config.py
import sqlite3

# a constant equal to a hash that contains the connection to the database
CONN = sqlite3.connect('company.db') 

# a constant that allows us to interact with the database and execute SQL commands 
CURSOR = CONN.cursor()
