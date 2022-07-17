from flask import Flask

from dotenv import load_dotenv
from redis import Redis
from rq import Queue


def create_app():
    app = Flask(__name__)
    load_dotenv('../env')
    q = Queue(connection=Redis())
    r = Redis(host='localhost', port=6379, db=0,
              charset='utf8', decode_responses=True)

    def increment():
        if r.get('count') is None:
            r.set('count', 1)
        r.incr('count')

    @app.route('/visit')
    def visit():
        count = q.enqueue(increment)
        return str(count)


    @app.route('/')
    def index():
        q.enqueue(increment)
        count = r.get('count')
        print(count)
        return '<h1>{}</h1>'.format(count)
    return app
