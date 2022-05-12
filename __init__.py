from flask import Flask, request, jsonify
import time
import redis
from rq import Queue
from .myworkers import *

app= Flask(__name__)

q = Queue(connection=redis.Redis(),default_timeout=3600)

@app.route('/refinance-bot',methods=["GET","POST"])
def fillRefinanceForm():
    data = request.json
    job = q.enqueue(HomeEquityQuizForm,data)
    datas = {"status":"success","queued_id": job.id , "queued_at" : job.enqueued_at}
    return datas


@app.route('/queue/status')
def CountQueues():
    return str(len(q.jobs))

if __name__=='__main__':
    app.run()