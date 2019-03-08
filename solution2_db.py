#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view result1 as select author,\
        concat('/article/',slug) as sl1 from articles")
    c.execute("create view name as select path , count(*)\
     as num from log Join result1 on result1.sl1 like log.path group\
        by path order by num desc")
    c.execute("create view name1 as select author,num from name\
     Join result1 on result1.sl1 like name.path order by num desc")
    c.execute("select name,sum(num) from name1 Join authors on\
     authors.id=name1.author group by name order by sum desc")
    data = c.fetchall()
    db.close()
    return data
