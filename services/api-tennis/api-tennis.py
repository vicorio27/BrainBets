from services.services import get
from constant import API_TENNIS, TIME_ZONE


def get_events():
    params = {
        "method": API_TENNIS["METHOD_GET_EVENTS"],
        "APIkey": API_TENNIS["APIKEY"],
    }
    response = get(url=API_TENNIS["API"], query_params=params)
    return response


def get_get_tournaments():
    params = {
        "method": API_TENNIS["METHOD_GET_TOURNAMENTS"],
        "APIkey": API_TENNIS["APIKEY"],
    }
    response = get(url=API_TENNIS["API"], query_params=params)
    return response


def get_fixtures(params: dict):
    response = get(url=API_TENNIS["API"], query_params=params)
    return response


def get_fixtures(
    date_start: str,
    date_stop: str,
    event_type_key: str,
    tournament_key: str,
    match_key: str,
    player_key: str,
):
    params = {
        "method": API_TENNIS["METHOD_GET_FIXTURES"],
        "APIkey": API_TENNIS["APIKEY"],
        "timezone": TIME_ZONE,
    }
    if date_start and date_stop:
        params["date_start"] = date_start
        params["date_stop"] = date_stop
    elif event_type_key:
        params["event_type_key"] = event_type_key
    elif tournament_key:
        params["tournament_key"] = tournament_key
    elif match_key:
        params["match_key"] = match_key
    elif player_key:
        params["player_key"] = player_key

    return get_fixtures(params=params)


def get_live_scores(params: dict):
    response = get(url=API_TENNIS["API"], query_params=params)
    return response


def get_live_scores(
    event_type_key: str, tournament_key: str, match_key: str, player_key: str
):
    params = {
        "method": API_TENNIS["METHOD_GET_LIVESCORE"],
        "APIkey": API_TENNIS["APIKEY"],
        "timezone": TIME_ZONE,
    }
    if event_type_key:
        params["event_type_key"] = event_type_key
    elif tournament_key:
        params["tournament_key"] = tournament_key
    elif match_key:
        params["match_key"] = match_key
    elif player_key:
        params["player_key"] = player_key

    return get_live_scores(params=params)


def get_H2H(first_player_key: str, second_player_key: str):
    params = {
        "method": API_TENNIS["METHOD_H2H"],
        "APIkey": API_TENNIS["APIKEY"],
        "first_player_key": first_player_key,
        "second_player_key": second_player_key,
    }
    response = get(url=API_TENNIS["API"], query_params=params)
    return response


def ranking(event_type: str):
    params = {
        "method": API_TENNIS["METHOD_STANDINGS"],
        "APIkey": API_TENNIS["APIKEY"],
        "event_type": event_type,  #'ATP' or 'WTA'
    }
    response = get(url=API_TENNIS["API"], query_params=params)
    return response


def players(player_key: str, tournament_key: str):
    params = {
        "method": API_TENNIS["METHOD_PLAYERS"],
        "APIkey": API_TENNIS["APIKEY"],
        "player_key": player_key,
        "tournament_key": tournament_key,
    }
    response = get(url=API_TENNIS["API"], query_params=params)
    return response
