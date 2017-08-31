import json
import urllib.request
import config
import constants

class RiotAPI(object):
    """ Riot API class is an interface for making calls to the Riot APIs """

    # Constant dictionary for HTTP Get uri
    URI = {
        "champ_list" : "https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&tags=all&dataById=false&api_key={}",
        "champ_detail" : "https://na1.api.riotgames.com/lol/static-data/v3/champions/{}?locale=en_US&tags=all&api_key={}"
        "recent_matchs" : "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{}/recent?api_key={}",
        "detail_match" : "https://na1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}",
        "player" : "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}",
        "current" : "https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/{}?api_key={}"
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
        # possibly? return list with [HTTP Code, Payload] instead of just payload
        return resp.read()

    @staticmethod
    def getChampionJSON():
        """
        IN: NONE
        Out: String - URI
        Desc: Static method for getting the list of champions in JSON format from Riot API
              Uses HTTP Get to send request
        """
        champURL = RiotAPI.__generateURI("champ_list")
        champJSON = RiotAPI.__doHTTPGetReq(champURL)
        return champJSON

    @staticmethod
    def getChampionJSON(champion_id):
        """
        IN: champion_id
        Out: String - URI
        Desc: Static method for getting the list of champions in JSON format from Riot API
              Uses HTTP Get to send request
        """
        champURL = RiotAPI.__generateURI("champ_detail")
        champJSON = RiotAPI.__doHTTPGetReq(champURL)
        return champJSON

    @staticmethod
    def getRecentMatchJSON(account_id):
        """
        IN: integer - account_id
        Out: String - URI
        Desc: Static method for getting a list of the last 20 matches played in JSON format from Riot API.
              Uses HTTP Get to send request
        """
        matchURL = RiotAPI.__generateURI("recent_matchs", account_id)
        matchJSON = RiotAPI.__doHTTPGetReq(matchURL)
        return matchJSON

    @staticmethod
    def getDetailMatchJSON(match_id):
        """
        IN: integer - match_id
        Out: String - URI
        Desc: Static method for getting a detailed information for the match id provided.
              Uses HTTP Get to send request
        """
        matchURL = RiotAPI.__generateURI("detail_match", match_id)
        matchJSON = RiotAPI.__doHTTPGetReq(matchURL)
        return matchJSON

    @staticmethod
    def getCurrentMatchJSON(summoner_id):
        """
        IN: integer - summoner_id
        Out: String - URI
        Desc: Static method for getting a detailed information for a match current being played.
              Uses HTTP Get to send request
        """
        matchURL = RiotAPI.__generateURI("detail_match", summoner_id)
        matchJSON = RiotAPI.__doHTTPGetReq(matchURL)
        return matchJSON

    @staticmethod
    def getPlayerJSON(summoner_name):
        """
        IN: String - summoner_id
        Out: String - URI
        Desc: Static method for getting summoner data in JSON formation from Riot API.
              Uses HTTP Get to send request
        """
        playerURL = RiotAPI.__generateURI("player", summoner_name)
        playerJSON = RiotAPI.__doHTTPGetReq(playerURL)
        return playerJSON
