import logging

from flask import render_template, Flask

app = Flask(__name__)
# 出力レベルをDEBUGに指定
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def home():
    logging.debug("Debug message")
    logging.info("Information message")
    logging.warning("Warning message")
    logging.error("Error message")
    logging.critical("Critical message")

    message = 'Logging Sample'
    return render_template('index.html', message=message)


@app.errorhandler(404)
def error_404(exception):
    logging.exception(exception)
    return {'message': 'Error: Resource not found.'}, 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
