import json

from flask import Flask, render_template
from flask import jsonify, request
from flask import make_response

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/sign", methods=['post'])
def sign():
    user = request.json;
    response = {
        'name' : user['name'],
        'email' : user['email'],
        'password' : user['password']
    }
    result = json.dumps(response, ensure_ascii=False)
    res = make_response(result)
    return res, 200

if __name__ == '__main__':
    app.run(port=4000)
