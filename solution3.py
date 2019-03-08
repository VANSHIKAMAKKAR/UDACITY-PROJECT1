#!/usr/bin/env python
from flask import Flask, request, redirect, url_for

from solution3_db import get_posts

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
    <head>
        <title>3rd qrery</title>
         </head>
    <body>
    <p>On which days did more than 1 &#37 of requests lead to errors?</p>
     <!-- post content will go here -->
        %s
        </center>
    </body>
</html>
'''
# HTML template for an individual comment
POST = '''\
        %s &nbsp; - &nbsp; %s &nbsp; error <br>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    posts = "".join(POST % (fdate, num) for fdate, num in get_posts())
    html = HTML_WRAP % posts
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
