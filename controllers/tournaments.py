import json

from flask import Blueprint

tournaments_api = Blueprint('tournaments_api', __name__)

@tournaments_api.route("/tournaments")
def tournaments():
    with open('./json/tournaments.json') as f:
        jtournament = json.load(f)

        return jtournament