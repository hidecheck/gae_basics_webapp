import logging

from flask import Flask, request

app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def home():
    return 'Cloud Scheduler Sample!'


@app.route('/run_job', methods=['POST'])
def run_job():
    logging.info('Running Schedule!!!')
    payload = request.get_data(as_text=True)
    logging.info('payload={}'.format(payload))
    return '', 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
