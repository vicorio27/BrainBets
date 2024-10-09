import json

from flask import Blueprint

players_api = Blueprint('players_api', __name__)

@players_api.route("/players")
def players():
    with open('./json/players.json') as f:
        jplayers = json.load(f)
        return jplayers