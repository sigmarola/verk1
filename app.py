#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from bottle import route, run
@route('/')
def home():
    return """<!DOCTYPE html>
            <html>
            <head>
                <title>Verk1</title>
            </head>
            <body>
                <h1>Halló heimur</h1>
                <a href="https://github.com/sigmarola/verk1">Github</a>
            </body>
            </html>"""

bottle.run(host='0.0.0.0', port=argv[1])


