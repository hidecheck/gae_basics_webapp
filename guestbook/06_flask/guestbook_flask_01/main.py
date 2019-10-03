from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    message = 'App Engine 勉強会 にようこそ'
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
