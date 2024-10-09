import json
import logging
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_swagger import swagger
from controllers import tournaments, players

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
app.register_blueprint(tournaments.tournaments_api)
app.register_blueprint(players.players_api)

cors = CORS(app)

logging.basicConfig(filename="test.log", level=logging.DEBUG)

VERSION = "1.0"

@app.route("/", methods=["GET"])
@cross_origin()
def spec():
    swag = swagger(app)
    swag["info"]["version"] = "1.0"
    swag["info"]["title"] = "My API"
    return jsonify(swag)

if __name__ == "__main__":
    app.run()
