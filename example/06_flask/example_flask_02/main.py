from flask import render_template, Flask


app = Flask(__name__)


@app.route('/')
def home():
    message = 'Hello World!'
    return render_template('index.html', message=message)


@app.errorhandler(404)
def error_404(exception):
    return {'message': 'Error: Resource not found.'}, 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
