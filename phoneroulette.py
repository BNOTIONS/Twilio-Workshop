from flask import Flask, request, render_template
from twilio import twiml
from random import choice

HOTLINE_NUMBER = '911'

phone_numbers = []

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' in request.form:
        phone_numbers.append(request.form['number'])
        return "Cool Thanks!!!!"
    else:
        return render_template('roulette.html', number=HOTLINE_NUMBER)


@app.route('/nums')
def numbers():
    return '<pre>' + '\n'.join(phone_numbers) + '</pre>'


@app.route('/phonecall')
def phonecall():
    phone_number = choice(phone_numbers)
    r = twiml.Response()
    r.dial(phone_number)
    return str(r)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
