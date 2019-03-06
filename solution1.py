from flask import Flask, request, redirect, url_for

from solution1_db import get_posts

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>1st QUERY</title>
    <style>
      h1, form { text-align: center; }
      body{background-color:#000;
      color:#FFF;
      }
      </style>
  </head>
  <body>
  <center>
    <h1>MOST VIEWED ARTICLES</h1>
    <table border="1px" cellspacing="0">  
    <tr>
    <th height="150" width="280">Title</th>
    <th height="150" width="280">Views</th>
    </tr>
    <!-- post content will go here -->
    %s
    </center>
  </body>
</html>
'''
# HTML template for an individual comment
POST ='''\
<tr>
<td height="150" width="280">%s</td>
<td height="150" width="250">%s</td>
</tr>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  posts = "".join(POST % (title,num) for title,num in get_posts())
  html = HTML_WRAP % posts
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
