import os
from celery import Celery

# Celeryからパスを通す
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.develop')
#
app = Celery('config')

# 設定のプレフィックスを設定
app.config_from_object('django.conf:settings', namespace='CELERY')
# タスク監視
app.autodiscover_tasks()
