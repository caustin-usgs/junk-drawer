from flask import Flask
from flask import jsonify
from flask import request
from api.ordering.version0 import API

app = Flask(__name__)
api = API()

@app.route('/')
def index():
    return 'hello world!'

@app.route('/api')
def api_versions():
  return jsonify(api.api_versions())

@app.route('/api/v<version>')
def api_info(version):

    info_dict = {
        '0': {
            'description': 'Version 0 of the ESPA API',
            'operations': {
                "/api": {
                    'function': "list versions",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0": {
                    'function': "list operations",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0/available-products/<product_ids>": {
                    'function': "list available products per sceneid",
                    'comments': "comma separated ids supported",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0/available-products": {
                    'function': "list available products per sceneid",
                    'comments': 'sceneids should be delivered in the product_ids parameter, comma separated if more than one',
                    'methods': [
                        "HEAD",
                        "POST"
                    ]
                },
                "/api/v0/projections": {
                    'function': "list available projections",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0/formats": {
                    'function': "list available output formats",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0/resampling-methods": {
                    'function': "list available resampling methods",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0/orders": {
                    'function': "list orders for authenticated user",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0/orders/<email>": {
                    'function': "list orders for supplied email, for user collaboration",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0/order/<ordernum>": {
                    'function': "retrieves a submitted order",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0/request/<ordernum>": {
                    'function': "retrieve order sent to server",
                    'methods': [
                        "HEAD",
                        "GET"
                    ]
                },
                "/api/v0/order": {
                    'function': "point for accepting processing requests via HTTP POST with JSON body. Errors are returned to user, successful validation returns an orderid",
                    'methods': [
                        "POST"
                    ]
                },
            }
        }
    }

    if info_dict.__contains__(version):
        response = info_dict[version]
    else:
        ver_str = ", ".join(info_dict.keys())
        err_msg = "%s is not a valid api version, these are: %s" % (version, ver_str)
        response = {"errmsg": err_msg}

    return_code = 200 if response.keys()[0] != "errmsg" else 401

    return jsonify(response), return_code

@app.route('/api/v0/available-products/<product_id>', methods=['GET'])
def available_prods_get(product_id):
    return jsonify(api.available_products(product_id))

@app.route('/api/v0/available-products', methods=['POST'])
def available_prods_post():
    x = request.form['product_ids']
    app.logger.debug(request.get_data())
    return jsonify(api.available_products(x))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)




