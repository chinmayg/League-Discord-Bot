import json
import urllib.request
import config

class RiotAPI(object):
    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def convertChampionIDtoName(champion_id):
        filename = "json/champion.json"
        with open(filename, 'r') as f:
            data = json.load(f)
            champ_data = data['data']
            for key in champ_data:
                details = champ_data[key]
                if int(details['key']) == champion_id:
                    return details['id']

    @staticmethod
    def getMatchJSON(account_id):
        matchURL = f"https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{account_id}/recent?api_key={config.riot_token}"
        req = urllib.request.Request(matchURL)
        resp = urllib.request.urlopen(req)
        matchJSON = resp.read()
        return matchJSON

    @staticmethod
    def getPlayerJSON(summoner_name):
        playerURL = f"https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{summoner_name}?api_key={config.riot_token}"
        req = urllib.request.Request(playerURL)
        resp = urllib.request.urlopen(req)
        playerJSON = resp.read()
        return playerJSON
