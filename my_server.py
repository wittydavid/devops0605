# what is flask
from flask import Flask, redirect, request

app = Flask(__name__)


# this is a decorator
# V
# What it does is connecting the REST api from a user requesy to the function that we want to run
@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        a = 1 / 0
        return '<font size=7>My name is Aviel</font>'
    elif request.method == 'POST':
        return 'creating your name'


app.run(host="0.0.0.0", port=5001, debug=True)
