from flask import Flask, abort, request, render_template


app = Flask(__name__)


@app.route('/')
def home():
    message = 'App Engine 勉強会 にようこそ'
    return render_template('index.html', message=message)


@app.route('/api/greetings', methods=['GET', 'POST'])
def greetings(key_id=None):
    if request.method == 'GET':
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
    abort(500)


@app.errorhandler(404)
def error_404(exception):
    return {'message': 'Error: Resource not found.'}, 404


@app.errorhandler(500)
def error_500(exception):
    return {'message': 'Please contact the administrator.'}, 500



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)