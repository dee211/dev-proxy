import redis
from tasks.request import get_response

r = redis.StrictRedis(host='localhost', port=6379, db=0)


class BaseHandler(object):
    def __init__(self, host):
        self.host = host

    def get(self, key):
        raise NotImplementedError


class CeleryHandler(BaseHandler):

    def get(self, key):
        value = self.get_value(key)
        if not value:
            self.set_task(key)
        return self.get_value(key) or 'error'

    def get_value(self, key):
        while r.get('in_process:{}'.format(key)):
            pass
        value = r.get('cache:{}:value'.format(key))
        return value

    def set_task(self, key):
        r.setex('in_process:{}'.format(key), 60, 1)
        get_response.delay(key=key, host=self.host)

    def reset_in_processed(self, key):
        r.delete('in_process:{}'.format(key))

    def set(self, key, value):
        r.setex('cache:{}:value'.format(key), 60 * 60 * 24, value)
        self.reset_in_processed(key)

