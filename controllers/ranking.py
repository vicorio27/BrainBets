import json

from flask import Blueprint

ranking_api = Blueprint("ranking_api", __name__)


@ranking_api.route("/ranking/<event_type>")
def ranking(event_type: str):
    """Ranking/Standings service specification.
    ---
    parameters:
    - name: event_type
    in: path
    type: string
    enum: ['ATP', 'WTA']
    required: true
    description: First player to compare
    definitions:
      Ranking:
        type: object
    responses:
      200:
        description: A list of Rankings
        schema:
          $ref: '#/definitions/Ranking'
        examples: {
            "success": 1,
            "result": [
                {
                        "event_type_key": "267",
                        "event_type_type": "Atp Doubles"
                },
                {
                        "event_type_key": "265",
                        "event_type_type": "Atp Singles"
                }
            ]
        }
    """
    with open("./json/events.json") as f:
        jevents = json.load(f)
        return jevents
