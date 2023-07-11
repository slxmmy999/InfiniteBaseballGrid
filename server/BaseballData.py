import requests

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

    def determine_possible_players(self):
        url = self.parse_api_url("a")
        data = requests.get(url)
        data = data.json()["people"][0]["stats"][-1]["splits"]
        for season in data:
            try:
                print(f"Year: {season['season']}, Team: {season['team']['name']}")
            except KeyError:
                continue

    def search_players(player):
        url = BaseballData.parse_api_url(player)
        data = requests.get(url)
        data = data.json()["people"]
        return data
    
    def get_player_teams(self, player):
        teams = []
        for item in player["stats"]:
            if item["type"]["displayName"] == "yearByYear":
                for season in item["splits"]:
                    try:
                        if season["team"]["name"] in teams:
                            continue
                        teams.append(season["team"]["name"])
                    except KeyError:
                        continue
        return teams

