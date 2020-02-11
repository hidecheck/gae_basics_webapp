from flask import Flask, render_template
from google.cloud import logging


app = Flask(__name__)


@app.route('/')
def home():
    # ロギングクライアントオブジェクトを取得
    logging_client = logging.Client()

    # ログネームを設定する
    logger = logging_client.logger('MyExampleApplication')

    # ログを出力する
    logger.log_text('Debug message', severity='DEBUG')
    logger.log_text('Information message', severity='INFO')
    logger.log_text('Warning message', severity='WARNING')
    logger.log_text('Error message', severity='ERROR')
    logger.log_text('Critical message', severity='CRITICAL')

    message = 'Logging Sample'
    return render_template('index.html', message=message)


@app.errorhandler(404)
def error_404(exception):
    # logging.exception(exception)
    return {'message': 'Error: Resource not found.'}, 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
