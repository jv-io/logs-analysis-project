#!/usr/bin/env python2.7.12

# "Database code" for the DB News.

import psycopg2
import bleach

DBNAME = "news"

print "\nRetrieving the 3 most popular articles of all time...\n"


def get_popnews():
    """Return the most popular three articles of all time.
    Sorted list with the most popular article at the top."""
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select * from popnews")
    data = c.fetchall()
    print("Title, Views:")
    for row in data:
        print(row)
    db.close()
    return


get_popnews()
print "\nSorting the authors based on popularity...\n"


def get_popauthor():
    """Return the most popular authors of all time.
    Sorted list with the most popular author at the top."""
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select * from popauthor")
    data = c.fetchall()
    print("Author, Views:")
    for row in data:
        print(row)
    db.close()
    return


get_popauthor()
print "\nShowing the days when more than 1% of requests led to errors...\n"


def get_errorcheck():
    """Return all days that had more than 1% of requests lead to errors.
    Sorted list with the most erroneous day at the top."""
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select * from errorcheck")
    data = c.fetchall()
    print("Date, Status, Percent:")
    for row in data:
        print(row)
    db.close()
    return


get_errorcheck()
print "\nThanks for viewing, have a great day!\n"
