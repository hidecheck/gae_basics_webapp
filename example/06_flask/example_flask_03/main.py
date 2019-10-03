from flask import render_template, Flask
from forms import MyForm


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    form = MyForm(csrf_enabled=False)
    if form.validate_on_submit():
        message = form.message.data
    else:
        message_validation_errors = form.errors.get('message')
        if message_validation_errors:
            message = message_validation_errors[0]  # 今回は0番目のエラーのみ表示する

    return render_template(
        'index.html',
        message=message,
        form=form,
    )


@app.errorhandler(404)
def error_404(exception):
    return {'message': 'Error: Resource not found.'}, 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
