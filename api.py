#!/usr/bin/python3
from flask import Flask, jsonify
from flask_cors import CORS

DEBUG=True

app = Flask(__name__)

CORS(app)
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'data': DATA
    })

DATA = [
    {	
    	'usuario': 'Pedro Perez',
        'id': '1',
        'producto': 'PC Gamer',
        'especificacion': '16 GB Ram, Intel icore7',
        'precio': '5000000',
        'cantidad': '2',
        'categoria': 'tecnologia',
        'avatar': 'https://i.blogs.es/ba8545/pcheap/450_1000.jpg'
    },
     {
        'usuario': 'Leonardo Quintero',
        'id': '2',
        'producto': 'Laptop',
        'especificacion': '12 GB Ram, Ryzen 5',
        'precio': '5200000',
        'cantidad': '5',
        'categoria': 'tecnologia',
        'avatar': 'https://images-na.ssl-images-amazon.com/images/I/613D0HzYeuL._AC_SY355_.jpg'
    },
      {
        'usuario': 'Nicolas Gonzales',
        'id': '3',
        'producto': 'Celulares Xiamoi',
        'especificacion': '128GB almcenamiento',
        'precio': '1000000',
        'cantidad': '9',
        'categoria': 'tecnologia',
        'avatar': 'https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/6/9/6941059646785_004.jpg'
    },
    {
        'usuario': 'Ximena Polania',
        'id': '4',
        'producto': 'Iphone 12',
        'especificacion': '64GB almacenamiento, color blanco',
        'precio': '4300000',
        'cantidad': '1',
        'categoria': 'tecnologia',
        'avatar': 'https://s1.eestatic.com/2019/11/12/actualidad/Actualidad_443967452_137772518_1706x960.jpg'
    },
    {
        'usuario': 'Maria Paula Cortes',
        'id': '5',
        'producto': 'Moto',
        'especificacion': 'Scooter electrica',
        'precio': '4000000',
        'cantidad': '1',
        'categoria': 'Movilidad',
        'avatar': 'https://www.comprascolectivas.com/1162/moto-electrica-starker-avanti-20-2019.jpg'
    },
    {
        'usuario': 'Mariana Parra',
        'id': '6',
        'producto': 'Bicicleta',
        'especificacion': 'Todo terreno, color blanco',
        'precio': '1500000',
        'cantidad': '2',
        'categoria': 'Movilidad',
        'avatar': 'https://cronicaglobal.elespanol.com/uploads/s1/23/08/86/5/bicicleta.jpeg'
    },
    {
        'usuario': 'Andres Felipe Gonzales',
        'id': '7',
        'producto': 'Parlante',
        'especificacion': 'Aiwa color negro-azul',
        'precio': '900000',
        'cantidad': '6',
        'categoria': 'tecnologia',
        'avatar': 'https://panamericana.vteximg.com.br/arquivos/ids/341920-600-690/parlante-bluetooth-aiwa-awsp08m-con-microfono-negro-2-7453041029500.jpg?v=637112332915130000'
    },
    {
        'usuario': 'valentina Molina',
        'id': '8',
        'producto': 'Gafas de sol',
        'especificacion': 'Marco negro, color negro',
        'precio': '420000',
        'cantidad': '3',
        'categoria': 'Indumentaria',
        'avatar': 'https://arturocalle.vteximg.com.br/arquivos/ids/211432-1200-1598/HOMBRE-GAFAS-10077954-NEGRO_1.jpg?v=636981319011600000'
    },
    {
        'usuario': 'Karen Sanchez',
        'id': '9',
        'producto': 'Cuadro',
        'especificacion': 'Partido en 3 20x20m',
        'precio': '1000000',
        'cantidad': '10',
        'categoria': 'Decoracion inmueble',
        'avatar': 'https://i.pinimg.com/originals/f8/5c/c8/f85cc840de622226560f8fb3b538aa4a.jpg'
    },
    {
        'usuario': 'Juan Jose Quintero',
        'id': '10',
        'producto': 'Zapato',
        'especificacion': 'Jhordan 1 gris',
        'precio': '800000',
        'cantidad': '2',
        'categoria': 'Indumentaria',
        'avatar': 'https://i.pinimg.com/originals/5a/55/d0/5a55d053e7a7c8f4aa06fa8030b99b25.jpg'
    },
    {
        'usuario': 'Daniela Gutierrez',
        'id': '11',
        'producto': 'Silla',
        'especificacion': 'Silla rosada de escritorio',
        'precio': '750000',
        'cantidad': '18',
        'categoria': 'Muebles',
        'avatar': 'https://ae01.alicdn.com/kf/HTB1is7oXITxK1Rjy0Fgq6yovpXa3.jpg_q50.jpg'
    },
    {
        'usuario': 'Mario Mendez',
        'id': '12',
        'producto': 'Chanclas',
        'especificacion': 'Color negro con blanco',
        'precio': '420000',
        'cantidad': '1',
        'categoria': 'Indumentaria',
        'avatar': 'https://i.pinimg.com/originals/da/f8/21/daf821ff26d76c127d682bd5b3e7137c.jpg'
    }
]


if __name__ == '__main__':
    app.run( host = '0.0.0.0',debug=True)

