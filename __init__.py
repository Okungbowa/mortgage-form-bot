from flask import Flask, request
import redis
from rq import Queue
from .myworkers import *
from input_data_model import BotInputModel

app = Flask(__name__)

q = Queue(connection=redis.Redis(), default_timeout=3600)


@app.route('/refinance-bot', methods=["GET", "POST"])
def fill_refinance_form():
    data = extract_json_data(request.json)
    job = q.enqueue(HomeEquityQuizForm, data)
    datas = {"status": "success", "queued_id": job.id, "queued_at": job.enqueued_at}
    return datas


@app.route('/queue/status')
def count_queues():
    return str(len(q.jobs))


def extract_json_data(json):
    model = BotInputModel(
        house_type=json['property_type'],
        credit_score=json['credit_grade'],
        property_value=json['home_val'],
        mort_balance=json['mortgage_balance'],
        mort_intr_rate=json['interest_rate'],
        loan_type=json['loan_type'],
        addtional_cash=json['add_cash'],
        bankruptcy=json['bankruptcy'],
        military_spouse=json['va_status'],
        home_improvements=json['home_improvements'],
        address=json['address'],
        zip_code=json['zip'],
        first_name=json['f_name'],
        last_name=json['l_name'],
        email_address=json['email'],
        phone=json['phone'],
        use_money=json['use_money'],
        dob=json['dob'],
        url=json['url'],
        refinance_purpose=json['refinance_purpose'],
        rate_type=json['rate_type'],
        state=json['state'],
        city=json['city'],
        current_lender=json['current_lender'],
        employed=json['employed'],
        last_ip=json['last_ip_used']
    )
    return model


if __name__ == '__main__':
    app.run()
