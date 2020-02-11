import logging

from flask import Flask, render_template
from google.cloud import logging as cloud_logging

# ロギングクライアントオブジェクトを取得
logging_client = cloud_logging.Client()

# ロギングハンドラーに結びつける
logging_client.setup_logging()

# ロギングハンドラーを取得する
log_handler = logging_client.get_default_handler()

# 名前をつけてロガーを取得する
logger = logging.getLogger("MyExampleApplication")

# 出力レベルをセットする
logger.setLevel(logging.DEBUG)


app = Flask(__name__)


@app.route('/')
def home():

    # ログを出力する
    logger.debug("Debug message")
    logger.info("Information message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

    message = 'Logging Sample'
    return render_template('index.html', message=message)


@app.errorhandler(404)
def error_404(exception):
    # logging.exception(exception)
    return {'message': 'Error: Resource not found.'}, 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
