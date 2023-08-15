import httpx
from urllib.parse import quote

class BaseballData:
    def __init__(self, catagories: list) -> None:
        self.catagories = catagories

    """ def validate_category(self): # returns invalid category(s) if any
        invalid = []

        for x in len(self.catagories):
            for y in len(self.catagories[x]):
                 """

    def parse_api_url(query):
        # In case player name is not URL safe
        safe_query = quote(query)
        return "https://statsapi.mlb.com/api/v1/people/search?names=" + safe_query + "&hydrate=awards,stats(group=[hitting,pitching],type=[career,yearByYear])"

    """ def determine_possible_players(self):
        url = self.parse_api_url("a")
        data = requests.get(url)
        data = data.json()["people"][0]["stats"][-1]["splits"]
        for season in data:
            try:
                print(f"Year: {season['season']}, Team: {season['team']['name']}")
            except KeyError:
                continue """

    @staticmethod
    async def search_players(player):
        if "'" in player:
            player = player.split("'")[0]
        url = BaseballData.parse_api_url(player)
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()["people"]
            return data
        
    @staticmethod    
    def __get_old_team_names(team):
        match(team):
            case "Cleveland Blues":
                return "Cleveland Guardians"
            case "Cleveland Bronchos":
                return "Cleveland Guardians"
            case "Cleveland Naps":
                return "Cleveland Guardians"
            case "Cleveland Indians":
                return "Cleveland Guardians"
            case "California Angels":
                return "Los Angeles Angels"
            case "Anaheim Angels":
                return "Los Angeles Angels"
            case "Los Angeles Angels of Anaheim":
                return "Los Angeles Angels"
            case "Florida Marlins":
                return "Miami Marlins"
            case "Tampa Bay Devil Rays":
                return "Tampa Bay Rays"
            case "Montreal Expos":
                return "Washington Nationals"
            # 1901-1960 Washington Senators became Minnesota Twins. 1961-1971 Washington Senators became current Rangers.
            case "Washington Senators":
                return "Minnesota Twins"
            # Milwaukee Brewers 1901-1901 are also part of the current Orioles franchise.
            # 1883-1898 St. Louis Browns became St. Louis Cardinals.  1902-1953 St. Louis Browns became Baltimore Orioles.
            case "St. Louis Browns":
                return "Baltimore Orioles"
            case "St. Louis Brown Stockings":
                return "St. Louis Cardinals"
            case "St. Louis Perfectos":
                return "St. Louis Cardinals"
            case "Cincinnati Red Stockings":
                return "Cincinnati Reds"
            case "Cincinnati Redlegs":
                return "Cincinnati Reds"
            case "Boston Red Stockings":
                return "Atlanta Braves"
            case "Boston Beaneaters":
                return "Atlanta Braves"
            case "Boston Doves":
                return "Atlanta Braves"
            case "Boston Rustlers":
                return "Atlanta Braves"
            case "Boston Bees":
                return "Atlanta Braves"
            case "Boston Braves":
                return "Atlanta Braves"
            case "Milwaukee Braves":
                return "Atlanta Braves"
            case "Brooklyn Atlantics":
                return "Los Angeles Dodgers"
            case "Brooklyn Grays":
                return "Los Angeles Dodgers"
            case "Brooklyn Grooms":
                return "Los Angeles Dodgers"
            # Bridegrooms overlapped with Grooms?
            # https://www.baseball-reference.com/teams/LAD/
            case "Brooklyn Bridegrooms":
                return "Los Angeles Dodgers"
            # Superbas and Robins overlapped with Dodgers?
            # https://www.baseball-reference.com/teams/LAD/
            case "Brooklyn Superbas":
                return "Los Angeles Dodgers"
            case "Brooklyn Robins":
                return "Los Angeles Dodgers"
            case "Brooklyn Dodgers":
                return "Los Angeles Dodgers"
            case "New York Gothams":
                return "San Francisco Giants"
            case "New York Giants":
                return "San Francisco Giants"
            case "New York Highlanders":
                return "New York Yankees"
            case "Philadelphia Athletics":
                return "Oakland Athletics"
            case "Kansas City Athletics":
                return "Oakland Athletics"
            case "Boston Americans":
                return "Boston Red Sox"
            case "Houston Colt .45s":
                return "Houston Astros"
            case "Philadelphia Quakers":
                return "Philadelphia Phillies"
            case "Seattle Pilots":
                return "Milwaukee Brewers"
            case "Chicago White Stockings":
                return "Chicago Cubs"
            case "Chicago Colts":
                return "Chicago Cubs"
            case "Chicago Orphans":
                return "Chicago Cubs"
            case "Pittsburgh Alleghenys":
                return "Pittsburgh Pirates"
            case _:
                return team
    
    @staticmethod
    def get_player_teams(player):
        teams = []
        for item in player["stats"]:
            if item["type"]["displayName"] == "yearByYear":
                for season in item["splits"]:
                    try:
                        if season["team"]["name"] in teams:
                            continue
                        teams.append(BaseballData.__get_old_team_names(season["team"]["name"]))
                    except KeyError:
                        continue
        return teams
    
    @staticmethod
    def get_player_picture(player=None, id=None):
        try:
            if not player and not id:
                raise ValueError("Must provide either player or id")
            if player:
                id = player['id']
            return f"https://img.mlbstatic.com/mlb-photos/image/upload/w_300,q_auto:best/v1/people/{id}/headshot/67/current"
        except KeyError:
            return ""
    
    @staticmethod
    async def lookup_by_id(id):
        async with httpx.AsyncClient() as client:
            url = f"https://statsapi.mlb.com/api/v1/people/{id}"
            response = await client.get(url)
            data = response.json()
            return data
