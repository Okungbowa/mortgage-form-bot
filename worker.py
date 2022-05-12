import sys
sys.path.insert(0, '<PATH_TO_PROJECT>')
import redis
from rq import Worker, Queue, Connection
conn = redis.Redis(host="redis-caching", port="6379")
listen = ['default']
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()