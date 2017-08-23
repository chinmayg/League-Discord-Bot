import json
from match import Match
from riot_api import RiotAPI

class Player(object):
    """ Player class represents and stores all of the Summoner data """
    def __init__(self, icon = None, player_name = None, level = None, account_id = None, match_history = None, summoner_id = None, timestamp = None):
        self.icon = icon
        self.player_name = player_name
        self.account_id = account_id
        self.summoner_id = summoner_id
        self.level = level
        self.timestamp = timestamp
        self.match_history = match_history

    def convertPlayerJSONtoPlayer(self, player_json):
        """ Converts Summoner JSON data from Riot"""
        data = json.loads(player_json)
        self.player_name = data['name']
        self.account_id =  data['accountId']
        self.summoner_id = data['id']
        self.level = data['summonerLevel']
        self.icon = data['profileIconId']
        self.timestamp = data['revisionDate']

    def convertMatchHistJSONtoMatchHistList(self, match_history_json):
        """ Converts the match_history JSON data from Riot to list"""
        if self.match_history is None:
            self.match_history = []

        data = json.loads(match_history_json)
        for single_match in data['matches']:
            match = Match(single_match["timestamp"], single_match["lane"],
                          single_match["champion"], single_match["role"],
                          single_match["gameId"])
            self.match_history.append(match)
