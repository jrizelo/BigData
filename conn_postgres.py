#!/usr/bin/python
hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'postgres'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT name, fone FROM emp" )

    for name, fone in cur.fetchall() :
        print (name, fone)

print ("Using psycopg2…")
import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()
