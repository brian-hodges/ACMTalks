import sys
from bottle import route, run

@route('/')
def index():
    return "Hello World!"

run(host='0.0.0.0', port=int(sys.argv[1]))
