import logging

from flask import Flask, abort, request, render_template
from google.cloud import storage

import ds


app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def home():
    message = 'App Engine 勉強会 にようこそ'
    return render_template('index.html', message=message)


@app.route('/photos', methods=['GET', 'POST'])
def photos():
    if request.method == 'GET':
        client = storage.Client()
        bucket = client.get_bucket('<バケット名>')
        return render_template('photos.html', blobs=bucket.list_blobs())
    else:
        uploaded_file = request.files['file']
        client = storage.Client()
        bucket = client.get_bucket('<バケット名>')
        blob = bucket.blob(uploaded_file.filename)
        blob.upload_from_file(uploaded_file)
        return render_template('complete.html')


@app.route('/api/greetings/<key_id>', methods=['GET', 'PUT', 'DELETE'])
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

    elif request.method == 'PUT':
        entity = ds.get_by_id(key_id)
        if not entity:
            abort(404)
            return entity

        entity['author'] = request.json['author']
        entity['message'] = request.json['message']
        entity = ds.update(entity)
        return entity

    elif request.method == 'DELETE':
        ds.delete(key_id)
        return '', 204


@app.route('/api/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'GET':
        parent_id = request.args['parent_id']
        entities = ds.get_comments(parent_id)
        res = {
            'comments': entities
        }
        return res, 200

    elif request.method == 'POST':
        parent_id = request.json['parent_id']
        message = request.json['message']
        entity = ds.insert_comment(parent_id, message)
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