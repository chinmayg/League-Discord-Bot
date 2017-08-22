import json
import urllib.request
import config
import constants

class RiotAPI(object):
    """ Riot API class is an interface for making calls to the Riot APIs """

    # Constant dictionary for HTTP Get uri
    URI = {
        "champ_list" : "https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&tags=all&dataById=false&api_key={}",
        "recent_matchs" : "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{}/recent?api_key={}",
        "detail_match" : "https://na1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}",
        "player" : "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}"
    }

    def __init__(self):
        self.champion_list = json.loads(RiotAPI.getChampionJSON())

    def convertChampionIDtoName(self, champion_id):
        """ Converts champion id from match history to champion name """
        champData = self.champion_list['keys']
        return champData[f'{champion_id}']

    @staticmethod
    def __generateURI(uri_token, param = None):
        """ Static Private method to generate URI for doing an HTTP Get """
        if param is None:
            return RiotAPI.URI[uri_token].format(config.riot_token)
        else:
            return RiotAPI.URI[uri_token].format(param, config.riot_token)

    @staticmethod
    def __doHTTPGetReq(url):
        """ Static private method for doing the HTTP get operation """
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        return resp.read()

    @staticmethod
    def getChampionJSON():
        """ Static method for getting the list of champions in JSON format from Riot API
            Uses HTTP Get to send request
        """
        champURL = RiotAPI.__generateURI("champ_list")
        champJSON = RiotAPI.__doHTTPGetReq(champURL)
        return champJSON

    @staticmethod
    def getRecentMatchJSON(account_id):
        """ Static method for getting a list of the last 20 matches played in JSON format from Riot API.
            Uses HTTP Get to send request
        """
        matchURL = RiotAPI.__generateURI("recent_matchs", account_id)
        matchJSON = RiotAPI.__doHTTPGetReq(matchURL)
        return matchJSON

    @staticmethod
    def getDetailMatchJSON(match_id):
        """ Static method for getting a detailed information for the match id provided.
            Uses HTTP Get to send request
        """
        matchURL = RiotAPI.__generateURI("detail_match", match_id)
        matchJSON = RiotAPI.__doHTTPGetReq(matchURL)
        return matchJSON

    @staticmethod
    def getPlayerJSON(summoner_name):
        """ Static method for getting summoner data in JSON formation from Riot API.
            Uses HTTP Get to send request
        """
        playerURL = RiotAPI.__generateURI("player", summoner_name)
        playerJSON = RiotAPI.__doHTTPGetReq(playerURL)
        return playerJSON
