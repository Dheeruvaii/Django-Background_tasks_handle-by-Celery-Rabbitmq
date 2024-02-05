from __future__ import absoulute_import,unicode_literals

from celery import shared_task

@shared_task
"""decorator to define shared apps over multiple django apps'"""

def add(x,y):
    return x*y

