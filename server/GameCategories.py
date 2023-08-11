import random

class GameCategories:
    choices = [
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/109.svg", "Arizona Diamondbacks"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/110.svg", "Baltimore Orioles"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/112.svg", "Chicago Cubs"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/113.svg", "Cincinnati Reds"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/115.svg", "Colorado Rockies"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/117.svg", "Houston Astros"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/108.svg", "Los Angeles Angels"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/146.svg", "Miami Marlins"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/142.svg", "Minnesota Twins"),   
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/147.svg", "New York Yankees"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/143.svg", "Philadelphia Phillies"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/135.svg", "San Diego Padres"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/137.svg", "San Francisco Giants"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/136.svg", "Seattle Mariners"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/139.svg", "Tampa Bay Rays"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/140.svg", "Texas Rangers"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/141.svg", "Toronto Blue Jays"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/120.svg", "Washington Nationals"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/144.svg", "Atlanta Braves"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/111.svg", "Boston Red Sox"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/145.svg", "Chicago White Sox"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/114.svg", "Cleveland Guardians"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/116.svg", "Detroit Tigers"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/118.svg", "Kansas City Royals"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/119.svg", "Los Angeles Dodgers"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/158.svg", "Milwaukee Brewers"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/121.svg", "New York Mets"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/133.svg", "Oakland Athletics"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/134.svg", "Pittsburgh Pirates"),
        ("https://www.mlbstatic.com/team-logos/team-cap-on-dark/138.svg", "St. Louis Cardinals"),
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
    
    @staticmethod
    def get_matchups(categories: list[list[tuple]]) -> list[tuple]:
        teams_top, teams_left = (categories[0], categories[1])
        matchups = [(top[1], left[1]) for top in teams_top for left in teams_left]
        return matchups

    def __str_(self) -> str:
        return str(self.categories)