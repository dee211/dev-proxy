import json
import urllib
import urllib2
from tasks import celery


@celery.task(ignore_result=True)
def get_response(key, host):
    from handlers import CeleryHandler
    handler = CeleryHandler(host)
    params = urllib.urlencode({'key': key})
    try:
        response = urllib2.urlopen("{}?{}".format(host, params))
        parsed_res = json.loads(response.read())
        if parsed_res and 'hash' in parsed_res:
            value = parsed_res['hash']
            handler.set(key, value)
            return value
    except (urllib2.URLError, urllib2.HTTPError) as e:
        error = 'error {}'.format(e.message)
        handler.reset_in_processed(key)
        return error
