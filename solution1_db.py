#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view result as select title\
        ,concat('/article/',slug) as sl from articles")
    c.execute("create view name as select path , count(*)\
     as num from log Join result on result.sl like log.path\
      group by path order by num desc limit 3")
    c.execute("select title,num from name Join result on\
     result.sl like name.path order by num desc")
    data = c.fetchall()
    db.close()
    return data
