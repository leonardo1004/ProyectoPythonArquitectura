from flask import Flask

app = Flask(__name__)


@app.route('/productos',methods=['GET'])
def Mostrar():
        return jsonify({[{"id": 1,"nombre": "El sexto sentido","director": "M. Night Shyamalan","clasificacion": "Drama"}]})

@app.route('/crear', methods=['POST'])
def Crear():
        return "Producto creado";

if __name__=="__main__":
 app.run(host = '0.0.0.0')
