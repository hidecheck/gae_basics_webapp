import logging

from flask import Flask, abort, request, render_template

app = Flask(__name__)
# 出力レベルをDEBUGに指定
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def home():
    message = 'App Engine 勉強会 にようこそ'
    return render_template('index.html', message=message)


@app.route('/api/greetings/<key_id>')
@app.route('/api/greetings', methods=['GET', 'POST'])
def greetings(key_id=None):
    if request.method == 'GET':
        if key_id:
            igarashi = {
                'id': 1,
                'author': 'Tsuyoshi Igarashi',
                'message': 'Hello'
            }
            return igarashi
        else:
            igarashi = {
                'id': 1,
                'author': 'Tuyoshi Igarashi',
                'message': 'Hello'
            }
            miyayama = {
                'id': 2,
                'author': 'Ryutaro Miyayama',
                'message': 'Looks good to me'
            }
            greetings = [igarashi, miyayama]
            res = {
                'greetings': greetings
            }
            return res
    elif request.method == 'POST':
        payload = request.get_json()
        res = {
            'id': 999,
            'author': payload['author'],
            'message': payload['message']
        }
        return res, 201


@app.route('/err500')
def err500():
    # 500エラーを返す
    abort(500)


@app.errorhandler(404)
def error_404(exception):
    logging.exception(exception)
    return {'message': 'Error: Resource not found.'}, 404


@app.errorhandler(500)
def error_500(exception):
    logging.exception(exception)
    return {'message': 'Please contact the administrator.'}, 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)