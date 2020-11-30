import flask
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG=True

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app)

@app.route('/Productos',methods=['GET'])
def Mostrar():
        return jsonify({[{"id": 1,"nombre": "El lllsexto sentido","director": "M. Night Shyamalan","clasificacion": "Drama"}]})

@app.route('/crear', methods=['POST'])
def Crear():
        return "Producto creado";

if __name__=="__main__":
 app.run(host = '0.0.0.0', debug=True)
