import logging

from flask import Flask, abort, request, render_template

import ds


app = Flask(__name__)
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
            entity = ds.get_by_id(key_id)
            if not entity:
                abort(404)
            return entity

        greetings = ds.get_all()

        res = {
            'greetings': greetings
        }
        return res

    elif request.method == 'POST':
        author = request.json['author']
        message = request.json['message']
        entity = ds.insert(author, message)
        return entity, 201


@app.route('/err500')
def err500():
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