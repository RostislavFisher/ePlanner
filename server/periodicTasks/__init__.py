import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

CELERYBEAT_SCHEDULE = {
    'task-name': {
        'task': 'periodicTasks.test',  # instead 'show'
        'schedule': crontab(minute='*/1'),
        # 'args': (42,),
    },
}
