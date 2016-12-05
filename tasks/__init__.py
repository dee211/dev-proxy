from dev import proxy_app
from run_celery import make_celery

celery = make_celery(proxy_app)
