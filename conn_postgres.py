#!/usr/bin/python
hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'postgres'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    
    novo_rec = "insert into emp values ((select max(id) +1 from emp), 'Jose da Silva', '51987655521', '1')"
    cur.execute(novo_rec)
    cur.execute( "SELECT name, fone FROM emp" )

    for name, fone in cur.fetchall() :
        print (name, fone)

print ("Using psycopg2…")
import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.commit()
myConnection.close()

import pgdb
myConnection1 = pgdb.Connection( host=hostname, user=username, password=password, database=database )
doQuery( myConnection1 )
myConnection1.commit()
myConnection1.close()

