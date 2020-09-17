import os
from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.deploy')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

from django.conf import settings

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))


