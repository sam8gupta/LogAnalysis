#!/usr/bin/env python
import psycopg2


def get_popular_articles(number, c):
    """Print most popular articles from the 'database', """
    """most recent first and 'number' in total."""
    c.execute(
        "select D.title, count(*) as views "
        "from vw_ArticleDetails as D, vw_ValidRequests as V "
        "where D.location = V.path "
        "group by D.title "
        "order by 2 desc "
        "limit (%s);", (number,)
        )
    rows = c.fetchall()
    for row in rows:
        print('"{0}" -- {1} views'.format(row[0], row[1]))


def get_popular_authors(c):
    """Print most popular authors from the 'database',
    most recent first and 'number' in total."""
    c.execute(
        "select A.name, count(*) as views "
        "from vw_ArticleDetails as D, vw_ValidRequests as V, authors as A "
        "where D.location = V.path and D.author = A.id "
        "group by A.name "
        "order by 2 desc;"
        )
    rows = c.fetchall()
    for row in rows:
        print('{0} -- {1} views'.format(row[0], row[1]))


def get_error_days(c):
    """Print the days from the 'database'
    when more than 1% of requests lead to errors,
    with the error percentage."""
    c.execute(
        "select A.date, round ((B.count*100)/A.count::DECIMAL, 2) as error"
        " from vw_Requests as A, vw_Requests as B"
        " where A.status = '200 OK' and B.status != '200 OK'"
        " and A.date=B.date and B.count*100>A.count;"
        )
    rows = c.fetchall()
    for row in rows:
        print('{0} -- {1}% errors'.format(row[0], row[1]))


print(
    "Welcome to the Reporting Tool:"
    "\nLet us grab some answers from the tool!!!\n"
    "\n1. What are the most popular three articles of all time?\n")

try:
    # connecting to database to execute the queries
    db = psycopg2.connect(database="news")
    cursor = db.cursor()
    print("The most popular three articles of all time are:")
    get_popular_articles(3, cursor)

    print("\n2. Who are the most popular article authors of all time?\n")
    print("The most popular article authors of all time are:")
    get_popular_authors(cursor)

    print("\n3. On which days did more than 1% of requests lead to errors?\n")
    print("The days on which more than 1% of requests lead to errors are:")
    get_error_days(cursor)

    db.close()


except:
    print ("Unable to connect to the database")
