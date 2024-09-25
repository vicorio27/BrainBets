import logging
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_swagger import swagger
from constant import RETURNING_STATES

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"

cors = CORS(app)

logging.basicConfig(filename="test.log", level=logging.DEBUG)


@app.route("/", methods=["GET"])
@cross_origin()
def spec():
    swag = swagger(app)
    swag["info"]["version"] = "1.0"
    swag["info"]["title"] = "My API"
    return jsonify(swag)


# Using list comprehension to iterate through loop
# list comprehensions are quite faster than for loop.
@app.route("/list", methods=["GET"])
@cross_origin()
def list_comprehension():
    list_comprehension_characteres = [
        character for character in RETURNING_STATES["FAIL"]
    ]
    return jsonify(list_comprehension_characteres)


if __name__ == "__main__":
    app.run()
