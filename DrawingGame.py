#! /usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/party/<party>')
def party_mode(party=None):
    return 'Not yet implemented, come back later bb'

@app.route('/')
def hello_world():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080)
