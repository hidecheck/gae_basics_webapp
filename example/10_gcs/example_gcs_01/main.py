import logging

from flask import render_template, request, Flask
from google.cloud import storage


app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        uploaded_file = request.files['file']
        client = storage.Client()
        bucket = client.get_bucket('gae-2nd-study')
        blob = bucket.blob(uploaded_file.filename)
        blob.upload_from_file(uploaded_file)
        return 'アップロードしました。'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
