import pybaseball
import requests

class BaseballData:
    def __init__(self, catagories: list) -> None:
        self.catagories = catagories

    """ def validate_category(self): # returns invalid category(s) if any
        invalid = []

        for x in len(self.catagories):
            for y in len(self.catagories[x]):
                 """

    def parse_api_url(self, query):
        return "https://statsapi.mlb.com/api/v1/people/search?names=" + query + "&hydrate=awards,stats(group=[hitting,pitching],type=[career,yearByYear])"

    def determine_possible_players(self):
        url = self.parse_api_url("a")
        data = requests.get(url)
        data = data.json()["people"][0]["stats"][-1]["splits"]
        for season in data:
            print(f"Year: {season['season']}, Team: {season['team']['name']}")