from handlers import CeleryHandler


class BaseRequester(object):
    handler_cls = NotImplemented

    def __init__(self, host):
        self.handler = self.handler_cls(host)

    def request(self, key):
        if self.is_invalid(key):
            return 'key is invalid'
        return self.handler.get(key)

    def is_invalid(self, key):
        raise NotImplementedError


class CeleryRequester(BaseRequester):
    handler_cls = CeleryHandler

    def is_invalid(self, key):
        return not key or not key.isdigit()
