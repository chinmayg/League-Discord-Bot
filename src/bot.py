import discord
from discord.ext import commands
import config
from player import Player
from riot_api import RiotAPI

description = """
        Hi! I am League bot! I can help you with the following:
            * Search a player's match history (Default last 2 matches)
        """
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def search(player_name = None, num_matches = 5):
    """Search for recent player match history"""

    if player_name is None:
        await bot.say("Please provide a summoner name/player name.\n See ?help search for usage.")
    else:
        summoner = Player()
        api = RiotAPI()

        playerJSON = RiotAPI.getPlayerJSON(player_name)
        summoner.convertPlayerJSONtoPlayer(playerJSON)

        matchJSON = RiotAPI.getRecentMatchJSON(summoner.account_id)
        summoner.convertMatchHistJSONtoMatchHistList(matchJSON)
        history = summoner.match_history

        if num_matches > 20:
            num_matches = 20
        printMatchList = history[0:num_matches]

        single_match = printMatchList[1]

        search_msg = f"In the last {num_matches} games, Summoner {player_name} has played:\n"
        count = 1
        for single_match in printMatchList:
            single_champ = api.convertChampionIDtoName(single_match.champion)
            date, time = single_match.pretty_timestamp().split()
            search_msg += f"#{count}: on {date} at {time}: {single_champ} \n"
            count++
        search_msg += "If you want to see detailed scoreboard for a game, use the command \"?detail {player_name} [Game_Number]\""
        await bot.say(search_msg)

@bot.command()
async def detail(player_name = None, game_num = 1):
    if player_name is None:
        await bot.say("Please provide a summoner name/player name.\n See ?help detail for usage.")
    else:
        # user will provide a number position that doesnt start at 0, normalize
        if game_num is 0:
            game_num = 1
            
        summoner = Player()
        api = RiotAPI()

        playerJSON = RiotAPI.getPlayerJSON(player_name)
        summoner.convertPlayerJSONtoPlayer(playerJSON)

        matchJSON = RiotAPI.getRecentMatchJSON(summoner.account_id)
        summoner.convertMatchHistJSONtoMatchHistList(matchJSON)
        history = summoner.match_history

        scoreboard = summoner.match_history[game_num - 1].printScoreboard()
        await bot.say(scoreboard)

bot.run(config.discord_token)
