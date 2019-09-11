from flask import Flask, jsonify, request, Response
import json
from flask_cors import CORS
import mysql.connector
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.secret_key = 'stock2shop secret key'
app.debug = True

CORS(app, resources={r"/*": {"origins": "*"}})

database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="stock2shop"
)

cur = database.cursor()

@app.route("/products", methods=['GET', 'POST'])
def endpoint_products():
    if request.method == 'GET':
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()
        parsed_products = {'results': []}

        for p in products:
            psku = p[1]
            pattributes = {}
            cur.execute("SELECT * FROM attributes where product_id={}".format(p[0]))
            attributes = cur.fetchall()
            for a in attributes:
                pattributes[a[2]] = a[3]
            product_obj = {'sku': psku, 'attributes': pattributes}
            parsed_products['results'].append(product_obj)
        return jsonify(parsed_products), 200

    elif request.method == 'POST':
        product_json = request.get_json()
        psku = product_json['sku']
        pattr = product_json['attributes']

        try:
            cur.execute("INSERT INTO products (sku) VALUES ('{}');".format(psku))
            database.commit()
        except TypeError as e:
            return jsonify({'error': e}), 418

        pid = cur.lastrowid
        
        for a in pattr:
            try:
                cur.execute("INSERT INTO attributes (product_id, attribute_key, attribute_value) VALUES ('{}', '{}', '{}');".format(pid, a['key'], a['value']))
                database.commit()
            except TypeError as e:
                return jsonify({'error': e}), 418

        return jsonify({'status': 'ok'}), 200

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Stock2Shop Documentation"

    swag['paths']['/products'] = {
        'get': {
            "tags": [
                "Request all products"
            ],
            "summary": "Returns all products",
            "responses": {
                "200": {
                    "description": "OK"
                }
            }
        },
        'post': {
            "tags": [
                "Creates a new product"
            ],
            "summary": "Creates a new product",
            "parameters": [
                {
                    "name": "sku",
                    "in": "path",
                    "required": "true",
                    "description": "Unique SKU for the product",
                    "type": "String"
                },
                {
                    "name": "attributes",
                    "in": "path",
                    "required": "true",
                    "description": "A list of attributes for the product. example: `{key: 'foo', value: 'bar'}`",
                    "type": "Array<Object>"
                }
            ],
            "responses": {
                "200": {
                    "description": "OK"
                }
            }
        }
    }

    return jsonify(swag)

SWAGGER_URL = '/documentation' 
API_URL = '/spec' 

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, 
    API_URL,
    config={
    'app_name': "Stock2Shop Application"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)