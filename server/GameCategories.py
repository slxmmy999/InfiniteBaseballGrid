import random

class GameCategories:
    choices = [
        ("~/static/dbacks.svg", "Arizona Diamondbacks"),
        ("~/static/orioles.svg", "Baltimore Orioles"),
        ("~/static/cubs.svg", "Chicago Cubs"),
        ("~/static/reds.svg", "Cincinnati Reds"),
        ("~/static/rockies.svg", "Colorado Rockies"),
        ("~/static/astros.svg", "Houston Astros"),
        ("~/static/angels.svg", "Los Angeles Angels"),
        ("~/static/marlins.svg", "Miami Marlins"),
        ("~/static/twins.svg", "Minnesota Twins"),   
        ("~/static/yankees.svg", "New York Yankees"),
        ("~/static/phil.svg", "Philadelphia Phillies"),
        ("~/static/padres.svg", "San Diego Padres"),
        ("~/static/giants.svg", "San Francisco Giants"),
        ("~/static/mariners.svg", "Seattle Mariners"),
        ("~/static/rays.svg", "Tampa Bay Rays"),
        ("~/static/rangers.svg", "Texas Rangers"),
        ("~/static/bluejays.svg", "Toronto Blue Jays"),
        ("~/static/nationals.svg", "Washington Nationals"),
        ("~/static/braves.svg", "Atlanta Braves"),
        ("~/static/redsox.svg", "Boston Red Sox"),
        ("~/static/whitesox.svg", "Chicago White Sox"),
        ("~/static/indians.svg", "Cleveland Indians"),
        ("~/static/tigers.svg", "Detroit Tigers"),
        ("~/static/royals.svg", "Kansas City Royals"),
        ("~/static/dodgers.svg", "Los Angeles Dodgers"),
        ("~/static/brewers.svg", "Milwaukee Brewers"),
        ("~/static/mets.svg", "New York Mets"),
        ("~/static/athletics.svg", "Oakland Athletics"),
        ("~/static/pirates.svg", "Pittsburgh Pirates"),
        ("~/static/cardinals.svg", "St. Louis Cardinals"),
        # ("nl", "National League"),
        # ("al", "American League")
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

    def get_grid(self):
        return self.categories

    def __str_(self) -> str:
        return str(self.categories)