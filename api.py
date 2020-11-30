<<<<<<< HEAD
from flask import Flask, jsonify
=======
from flask import Flask
from flask_cors import CORS
>>>>>>> leonardo

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/productos',methods=['GET'])
def Mostrar():
        return jsonify({[{"id": 1,"nombre": "El lllsexto sentido","director": "M. Night Shyamalan","clasificacion": "Drama"}]})

@app.route('/crear', methods=['POST'])
def Crear():
        return "Producto creado";

if __name__=="__main__":
 app.run(host = '0.0.0.0')
