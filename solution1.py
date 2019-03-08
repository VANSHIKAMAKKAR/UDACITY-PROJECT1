#!/usr/bin/env python
from flask import Flask, request, redirect, url_for

from solution1_db import get_posts

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
    <head>
         <title>1st QUERY</title>
    </head>
    <body>
            <p>What are the most popular three articles of all time?</p>
         <!-- post content will go here -->
        %s
        </body>
</html>
'''
# HTML template for an individual comment
POST = '''\
                     %s &nbsp; - &nbsp; %s &nbsp; views <br>
    '''


@app.route('/', methods=['GET'])
def main():
    posts = "".join(POST % (title, num) for title, num in get_posts())
    html = HTML_WRAP % posts
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
