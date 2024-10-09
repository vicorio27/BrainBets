import json

from flask import Blueprint

tournaments_api = Blueprint("tournaments_api", __name__)


@tournaments_api.route("/tournaments")
def tournaments():
    """Tournaments service specification.
    ---
    definitions:
      Tournament:
        type: object
    responses:
      200:
        description: A list of torunaments
        schema:
          $ref: '#/definitions/TournamentName'
        examples: {
        "success": 1,
        "result": [
                {
                        "tournament_key": "2833",
                        "tournament_name": "Aachen",
                        "event_type_key": "281",
                        "event_type_type": "Challenger Men Singles"
                },
                {
                        "tournament_key": "3872",
                        "tournament_name": "Abu Dhabi",
                        "event_type_key": "266",
                        "event_type_type": "Wta Singles"
                }
        ]
        }
    """
    with open("./json/tournaments.json") as f:
        jtournament = json.load(f)

        return jtournament
