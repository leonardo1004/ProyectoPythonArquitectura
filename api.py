#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'data': DATA
    })

DATA = [
    {
        'id': '1',
        'email': 'Jack@Kerouac',
        'first_name': 'Leo',
        'last_name': 'Qionte',
        'avatar': 'ergethtuk'
    },
     {
        'id': '2',
        'email': 'Jack@Keruac',
        'first_name': 'Nico',
        'last_name': 'gonze',
        'avatar': 'whqghhq'
    },
      {
        'id': '3',
        'email': 'Jack@Keroac',
        'first_name': 'ergerg',
        'last_name': 'wrgt4h',
        'avatar': 'rgwwhth'
    }
]


if __name__ == '__main__':
    app.run( host = '0.0.0.0')

