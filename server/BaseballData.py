import httpx

class BaseballData:
    def __init__(self, catagories: list) -> None:
        self.catagories = catagories

    """ def validate_category(self): # returns invalid category(s) if any
        invalid = []

        for x in len(self.catagories):
            for y in len(self.catagories[x]):
                 """

    def parse_api_url(query):
        return "https://statsapi.mlb.com/api/v1/people/search?names=" + query + "&hydrate=awards,stats(group=[hitting,pitching],type=[career,yearByYear])"

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
        url = BaseballData.parse_api_url(player)
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()["people"]
            return data
        
    @staticmethod    
    def __get_old_team_names(team):
        match(team):
            case "Cleveland Indians":
                return "Cleveland Guardians"
            case "California Angels":
                return "Los Angeles Angels"
            case "Anaheim Angels":
                return "Los Angeles Angels"
            case "Florida Marlins":
                return "Miami Marlins"
            case "Tampa Bay Devil Rays":
                return "Tampa Bay Rays"
            case "Montreal Expos":
                return "Washington Nationals"
            case "Washington Senators":
                return "Minnesota Twins"
            case "St. Louis Browns":
                return "Baltimore Orioles"
            case "Boston Braves":
                return "Atlanta Braves"
            case "Milwaukee Braves":
                return "Atlanta Braves"
            case "Brooklyn Dodgers":
                return "Los Angeles Dodgers"
            case "New York Giants":
                return "San Francisco Giants"
            case "New York Highlanders":
                return "New York Yankees"
            case "Philadelphia Athletics":
                return "Oakland Athletics"
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

    def get_player_picture(player):
        id = player['link'].split('/')[-1]
        return f"https://img.mlbstatic.com/mlb-photos/image/upload/w_300,q_auto:best/v1/people/{id}/headshot/67/current"