import logging
from flask import Flask, jsonify, json, request
from flask_api import status
from flask_cors import CORS, cross_origin
from flask_swagger import swagger


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

OK = 'OK'
FAIL = 'FAIL'

logging.basicConfig(filename="test.log", level=logging.DEBUG)

@app.route("/", methods=['GET'])
@cross_origin()
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

if __name__ == '__main__':
    app.run()