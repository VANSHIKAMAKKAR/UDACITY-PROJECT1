#!/usr/bin/env python
from flask import Flask, request, redirect, url_for

from solution2_db import get_posts

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
    <head>
        <title>2nd qrery</title>
         </head>
    <body>
    <p> Who are the most popular article authors of all time?</p>
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
    '''Main page of the forum.'''
    posts = "".join(POST % (name, num) for name, num in get_posts())
    html = HTML_WRAP % posts
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070)
