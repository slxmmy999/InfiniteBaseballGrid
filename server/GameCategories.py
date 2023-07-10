import random

class GameCategories:
    choices = [
        ("dbacks", "Arizona Diamondbacks"),
        ("orioles", "Baltimore Orioles"),
        ("cubs", "Chicago Cubs"),
        ("reds", "Cincinnati Reds"),
        ("rockies", "Colorado Rockies"),
        ("astros", "Houston Astros"),
        ("angels", "Los Angeles Angels"),
        ("marlins", "Miami Marlins"),
        ("twins", "Minnesota Twins"),   
        ("yankees", "New York Yankees"),
        ("phil", "Philadelphia Phillies"),
        ("padres", "San Diego Padres"),
        ("giants", "San Francisco Giants"),
        ("mariners", "Seattle Mariners"),
        ("rays", "Tampa Bay Rays"),
        ("rangers", "Texas Rangers"),
        ("bluejays", "Toronto Blue Jays"),
        ("nationals", "Washington Nationals"),
        ("braves", "Atlanta Braves"),
        ("redsox", "Boston Red Sox"),
        ("whitesox", "Chicago White Sox"),
        ("indians", "Cleveland Indians"),
        ("tigers", "Detroit Tigers"),
        ("royals", "Kansas City Royals"),
        ("dodgers", "Los Angeles Dodgers"),
        ("brewers", "Milwaukee Brewers"),
        ("mets", "New York Mets"),
        ("athletics", "Oakland Athletics"),
        ("pirates", "Pittsburgh Pirates"),
        ("cardinals", "St. Louis Cardinals"),
        ("nl", "National League"),
        ("al", "American League")
        # TODO: add more categories
    ]

    # create and then validate a 3D list of categories representing the grid
    def __init__(self) -> None:
        categories = []
        top = []
        bottom = []

        for _ in range(0, 3):
            choice = random.choice(self.choices)
            while choice in top or choice in bottom:
                choice = random.choice(self.choices)

            top.append(choice)

            choice = random.choice(self.choices)
            while choice in top or choice in bottom:
                choice = random.choice(self.choices)

            bottom.append(choice)

        categories.append(top)
        categories.append(bottom)

        self.categories = categories