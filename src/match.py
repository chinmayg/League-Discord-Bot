import time

class Match(object):
    """ This class will hold all information about a League of Legends match"""

    # Constructor
    def __init__(self, timestamp = None, lane = None, champion = None, role = None, gameId = None):
        self.timestamp = timestamp
        self.lane = lane
        self.champion = champion
        self.role = role
        self.gameId = gameId

    def pretty_timestamp(self):
        return time.strftime('%m-%d-%y %I:%M:%S', time.localtime(self.timestamp/1000))
