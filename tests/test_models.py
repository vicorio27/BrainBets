import json

from responses.response import Response
from models.event import Event

def test_event_wrapper():
    with open('../json/events.json') as f:
        jevetns = json.load(f)
        events = Response[Event](**jevetns)

