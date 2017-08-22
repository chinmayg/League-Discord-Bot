# Constant values from Riot
# REGIONS
RUSSIA = 'ru'
KOREA = 'kr'
BRAZIL = 'br1'
OCEANIA = 'oc1'
JAPAN = 'jp1'
NORTH_AMERICA = 'na1'
EUROPE_NORDIC_EAST = 'eun1'
EUROPE_WEST = 'euw1'
TURKEY = 'tr1'
LATIN_AMERICA_NORTH = 'la1'
LATIN_AMERICA_SOUTH = 'la2'

# SEASONS
seasons_id = {
    0 : 'PRESEASON 3',
    1 : 'SEASON 3',
    2 : 'PRESEASON 4',
    3 : 'SEASON 4',
    4 : 'PRESEASON 5',
    5 : 'SEASON 5',
    6 : 'PRESEASON 6',
    7 : 'SEASON 6',
    8 : 'PRESEASON 7',
    9 : 'SEASON 7'
}

# MATCHMAKING QUEUES
queue_types = {
    0 : 'CUSTOM',
    8 : 'NORMAL_3x3',
    2 : 'NORMAL_5x5_BLIND',
    14 : 'NORMAL_5x5_DRAFT',
    4 : 'RANKED_SOLO_5x5',
    9 : 'RANKED_FLEX_TT',
    42 : 'RANKED_TEAM_5x5',
    16 : 'ODIN_5x5_BLIND',
    17 : 'ODIN_5x5_DRAFT',
    25 : 'BOT_ODIN_5x5',
    32 : 'BOT_5x5_INTRO',
    32 : 'BOT_5x5_BEGINNER',
    33 : 'BOT_5x5_INTERMEDIATE',
    52 : 'BOT_TT_3x3',
    61 : 'GROUP_FINDER_5x5',
    65 : 'ARAM_5x5',
    70 : 'ONEFORALL_5x5',
    72 : 'FIRSTBLOOD_1x1',
    73 : 'FIRSTBLOOD_2x2',
    75 : 'SR_6x6',
    76 : 'URF_5x5',
    78 : 'ONEFORALL_MIRRORMODE_5x5',
    83 : 'BOT_URF_5x5',
    91 : 'NIGHTMARE_BOT_5x5_RANK1',
    92 : 'NIGHTMARE_BOT_5x5_RANK2',
    93 : 'NIGHTMARE_BOT_5x5_RANK5',
    96 : 'ASCENSION_5x5',
    98 : 'HEXAKILL',
    100 : 'BILGEWATER_ARAM_5x5',
    300 : 'KING_PORO_5x5',
    310 : 'COUNTER_PICK',
    313 : 'BILGEWATER_5x5',
    315 : 'SIEGE',
    317 : 'DEFINITELY_NOT_DOMINION_5x5',
    318 : 'ARURF_5X5',
    325 : 'ARSR_5x5',
    400 : 'TEAM_BUILDER_DRAFT_UNRANKED_5x5',
    420 : 'TEAM_BUILDER_RANKED_SOLO',
    430 : 'TB_BLIND_SUMMONERS_RIFT_5x5',
    440 : 'RANKED_FLEX_SR',
    600 : 'ASSASSINATE_5x5',
    610 : 'DARKSTAR_3x3'
}

# MAP NAMES
game_maps = [
    {'map_id': 1, 'name': "Summoner's Rift", 'notes': "Summer Variant"},
    {'map_id': 2, 'name': "Summoner's Rift", 'notes': "Autumn Variant"},
    {'map_id': 3, 'name': "The Proving Grounds", 'notes': "Tutorial Map"},
    {'map_id': 4, 'name': "Twisted Treeline", 'notes': "Original Version"},
    {'map_id': 8, 'name': "The Crystal Scar", 'notes': "Dominion Map"},
    {'map_id': 10, 'name': "Twisted Treeline", 'notes': "Current Version"},
    {'map_id': 11, 'name': "Summoner's Rift", 'notes': "Current Version"},
    {'map_id': 12, 'name': "Howling Abyss", 'notes': "ARAM Map"},
    {'map_id': 14, 'name': "Butcher's Bridge", 'notes': "ARAM Map"},
    {'map_id': 16, 'name': "Cosmic Ruins", 'notes': "Dark Star Map"},
]

# GAME/MATCH MODES
game_modes = [
    'CLASSIC',  # Classic Summoner's Rift and Twisted Treeline games
    'ODIN',  # Dominion/Crystal Scar games
    'ARAM',  # ARAM games
    'TUTORIAL',  # Tutorial games
    'ONEFORALL',  # One for All games
    'ASCENSION',  # Ascension games
    'FIRSTBLOOD',  # Snowdown Showdown games
    'KINGPORO',  # King Poro games
    'SIEGE',  # Nexus Siege games
    'ASSASSINATE',  # Blood Hunt Assassin games
    'ARSR',  # All Random Summoner's Rift games
    'DARKSTAR',  # Dark Star games
]

# GAME/MATCH TYPES
game_types = [
    'CUSTOM_GAME',  # Custom games
    'TUTORIAL_GAME',  # Tutorial games
    'MATCHED_GAME',  # All other games
]

# SUB TYPES
sub_types = [
    'NONE',  # Custom games
    'NORMAL',  # Summoner's Rift unranked games
    'NORMAL_3x3',  # Twisted Treeline unranked games
    'ODIN_UNRANKED',  # Dominion/Crystal Scar games
    'ARAM_UNRANKED_5v5',  # ARAM / Howling Abyss games
    'BOT',  # Summoner's Rift and Crystal Scar games played against AI
    'BOT_3x3',  # Twisted Treeline games played against AI
    'RANKED_SOLO_5x5',  # Summoner's Rift ranked solo queue games
    'RANKED_TEAM_3x3',  # Twisted Treeline ranked team games
    'RANKED_TEAM_5x5',  # Summoner's Rift ranked team games
    'ONEFORALL_5x5',  # One for All games
    'FIRSTBLOOD_1x1',  # Snowdown Showdown 1x1 games
    'FIRSTBLOOD_2x2',  # Snowdown Showdown 2x2 games
    'SR_6x6',  # Hexakill games
    'CAP_5x5',  # Team Builder games
    'URF',  # Ultra Rapid Fire games
    'URF_BOT',  # Ultra Rapid Fire games against AI
    'NIGHTMARE_BOT',  # Nightmare bots
    'ASCENSION',  # Ascension games
    'HEXAKILL',  # Twisted Treeline 6x6 Hexakill
    'KING_PORO',  # King Poro games
    'COUNTER_PICK',  # Nemesis games
    'BILGEWATER',  # Black Market Brawlers games
    'SIEGE',  # Nexus Siege games
    'RANKED_FLEX_TT',  # Ranked Flex Twisted Treeline games
    'RANKED_FLEX_SR',  # Ranked Flex Summoner's Rift games
    'DARKSTAR',  # Dark Star games
]

ranked_solo = 'RANKED_SOLO_5x5'
ranked_flex_sr = 'RANKED_FLEX_SR'
ranked_flex_tt = 'RANKED_FLEX_TT'
