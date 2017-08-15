import json
import urllib.request
import config

class RiotAPI(object):
    """ Riot API class is an interface for making calls to the Riot APIs """
    def __init__(self):
        self.champion_list = json.loads(RiotAPI.getChampionJSON())

    def convertChampionIDtoName(self, champion_id):
        """ Converts champion id from match history to champion name"""
        champData = self.champion_list['keys']
        return champData[f'{champion_id}']

    @staticmethod
    def __doHTTPGetReq(url):
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        return resp.read()

    @staticmethod
    def getChampionJSON():
        """ Static method for getting the list of champions in JSON format from Riot API
            Uses HTTP Get to send request
        """
        champURL = f"https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&tags=all&dataById=false&api_key={config.riot_token}"
        champJSON = RiotAPI.__doHTTPGetReq(champURL)
        return champJSON

    @staticmethod
    def getRecentMatchJSON(account_id):
        """ Static method for getting a list of the last 20 matches played in JSON format from Riot API.
            Uses HTTP Get to send request
        """
        matchURL = f"https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{account_id}/recent?api_key={config.riot_token}"
        matchJSON = RiotAPI.__doHTTPGetReq(matchURL)
        return matchJSON

    @staticmethod
    def getPlayerJSON(summoner_name):
        """ Static method for getting summoner data in JSON formation from Riot API.
            Uses HTTP Get to send request
        """
        playerURL = f"https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{summoner_name}?api_key={config.riot_token}"
        playerJSON = RiotAPI.__doHTTPGetReq(playerURL)
        return playerJSON
