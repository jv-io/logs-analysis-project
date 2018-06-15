#!/usr/bin/env python2.7.12
# "Database code" for the DB News.


# Imports psycopg2 so we can connect with the databse using psql
import psycopg2
# Imports  from_db_cursor so we can create a table from sql
from prettytable import from_db_cursor

# Defines the database name
DBNAME = "news"

# Defines the list of pre-query notices
notice = ["\nRetrieving the 3 most popular articles of all time...\n",
          "\nSorting the authors based on popularity...\n",
          "\nShowing the days when more than 1% of requests led to errors...\n"
          ]

# Defines the list of database queries
query = ["select * from popnews",
         "select * from popauthor",
         "select * from errorcheck"]


def execute_query(query_string):
    """Connects with the database, executes the query and prints out the table.
    Input:
        query_string(str)
        DBNAME(str)
    Behavior:
        Connects with the database.
        Creates a database cursor.
        Executes the database query.
        Creates a prettytable from database results.
        Prints the prettytable.
        Closes the database.
    Return:
        none
    """
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute(query_string)
    x = from_db_cursor(c)
    print (x)
    db.close()
    return


def search_db():
    """	Loops through queries and passes the right string on to execute_query.
    Input:
        query(list of strings)
        notice(list of strings)
    Behavior:
        Checks if we are within the total number_of_queries.
        Prints the corresponding notice.
        Creates the corresponding query_string variable.
        Forwards the query_string variable to execute_query.
        Update the counting variable.
    Return:
        none
    """
    number_of_queries = len(query) - 1
    query_number = 0

    while query_number <= number_of_queries:
        print notice[query_number]
        query_string = query[query_number]
        execute_query(query_string)
        query_number += 1
    else:
        print "\nThanks for viewing, have a great day!\n"
        exit()


# Runs all the queries through the database
print search_db()
