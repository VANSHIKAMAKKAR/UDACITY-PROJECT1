import psycopg2, bleach

DBNAME = "news"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("update articles set slug = concat('/article/',slug)")
  c.execute("create view name as select path , count(*) as num from log Join articles on articles.slug like log.path group by path order by num desc limit 3")
  c.execute("select title,num from name Join articles on articles.slug like name.path order by num desc")
  data= c.fetchall()
  db.close()
  return data