"""
Phoneroulette - Super tiny webapp that you can use to call
a random friend!
Last Updated 10.13.12 by Logan
"""
from flask import Flask, request, render_template
from twilio import twiml
from random import choice

# This number should be the number you hooked up on twilio
HOTLINE_NUMBER = '911'

# In a production app you'd want some sort of db, in-memory is cool for now
phone_numbers = []

# And here is our actual magic Flask app!
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    This is the main index page. It displays a number submission form,
    and adds the number to the list if the form submits.
    In a production application, we'd want some validation/deduplication!
    """
    if 'number' in request.form:
        phone_numbers.append(request.form['number'])
        return "Cool Thanks!!!!"
    else:
        return render_template('roulette.html', number=HOTLINE_NUMBER)


@app.route('/nums')
def numbers():
    """
    This is just a debug path that lists all the numbers we have in memory.
    A production app should probably not have this turned on!
    """
    return '<pre>' + '\n'.join(phone_numbers) + '</pre>'


@app.route('/phonecall')
def phonecall():
    """
    This is the path that Twilio hits when someone calls your phone number.
    It generates the TwiML that tells Twilio to call a number from the list.
    A production app would make sure you didn't call yourself, and probably
    retry if someone else had a busy signal.
    """
    phone_number = choice(phone_numbers)
    r = twiml.Response()
    r.dial(phone_number)
    return str(r)


# And this is where we run the App! Turning debug on lets us see errors
if __name__ == '__main__':
    app.run(port=5000, debug=True)
