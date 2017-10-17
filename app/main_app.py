#!/usr/bin/env python
import bottle
import os

app = bottle.app()

@bottle.route('/hello/<name>')
def index(name):
    return bottle.template('index',name=name)

@bottle.route('/json')
def json_reply():
    heads = bottle.request.headers
    bottle.response.content_type = 'application/json'

    response = {'headers':dict(heads),
            'environment':dict(os.environ),
            'response':dict(bottle.response.headers)}
    return response

if __name__=='__main__':
    bottle.debug(True)
    bottle.run(reloader=True,app=app,host='localhost',port=8080)