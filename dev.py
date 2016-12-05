from flask import Flask
from flask import request

proxy_app = Flask(__name__)
proxy_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',
    CELERY_IMPORTS=('tasks.request',)
)
HOST = 'https://vast-eyrie-4711.herokuapp.com/'


@proxy_app.route('/from_cache/')
def hello_world():
    key = request.args.get('key')
    from backend import CeleryRequester
    return CeleryRequester(HOST).request(key)
