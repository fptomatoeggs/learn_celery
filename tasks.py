from celery import Celery

# app = Celery('tasks', broker='amqp://guest@localhost//')
app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')
# app = Celery('tasks', broker='redis://localhost')

app.conf.CELERY_TASK_SERIALIZER = 'json'

@app.task
def add(x, y):
    return x + y
