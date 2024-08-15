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
        ("AVG300", ".300+ Average Season"), # Confirmed Viable
        ("HR40", "40+ Home Run Season"), # Confirmed Viable
        ("CY", "Cy Young Award Winner"), # Confirmed Viable - Rockies
        ("MVP", "MVP Award Winner"), # Confirmed Viable - Rays + Mets + Dbacks (get fucked mets lol)
        ("ROY", "Rookie of the Year Award Winner"), # Confirmed Viable - Diamondbacks + Padres
    ]

    # create and then validate a 3D list of categories representing the grid
    def __init__(self, mode) -> None:
        categories = []
        top = []
        bottom = []
        print(self.choices[:30])
        match(mode):
            case "players_only":
                for _ in range(0, 3):
                    choice = random.choice(self.choices[:30])
                    while choice in top or choice in bottom:
                        choice = random.choice(self.choices[:30])

                    top.append(choice)
                    
                    choice = random.choice(self.choices[:30])
                    while choice in top or choice in bottom:
                        choice = random.choice(self.choices[:30])

                    bottom.append(choice)

                categories.append(top)
                categories.append(bottom)

                self.categories = categories

            case "players_stats":
                for _ in range(0, 3):
                    choice = random.choice(self.choices)
                    while choice in top or choice in bottom:
                        choice = self.filter_stats_recursively(top, bottom, choice)

                    top.append(choice)

                    choice = random.choice(self.choices)
                    while choice in top or choice in bottom:
                        choice = self.filter_stats_recursively(top, bottom, choice)

                    bottom.append(choice)

                categories.append(top)
                categories.append(bottom)

                self.re_roll_unviable_stats()

                self.categories = categories
    def get_grid(self):
        return self.categories
    
    def __get_grid_opposers(grid, index):
        if index > 2:
            return grid[:2]
        else:
            return grid[2:]
  
    def filter_stats_recursively(self, top, bottom, choice) -> tuple:
        if choice[0].endswith(".svg") != True:
            while choice[0].endswith(".svg") != True:
                choice = random.choice(self.choices)
            if choice in top or choice in bottom:
                self.filter_stats_recursively(top, bottom, choice)
        return choice
    
    def re_roll_unviable_stats(self):
        for index, cat in enumerate(self.categories):
            cat: str = cat[0]
            if cat.endswith(".svg"):
                continue
            else:
                match(cat):
                    case "AVG300":
                        continue
                    case "HR40":
                        continue
                    case "CY":
                        for item in self.__get_grid_opposers(self.categories, index):
                            match(item[1]):
                                case "Colorado Rockies":
                                    while self.categories[index[1]] == "Colorado Rockies":
                                        self.categories[index] = random.choice(self.choices)
                                case _:
                                    continue
                    case "MVP":
                        prohibited_teams = ["Tampa Bay Rays", "New York Mets", "Arizona Diamondbacks"]
                        for item in self.__get_grid_opposers(self.categories, index):
                            match(item[1]):
                                case "Tampa Bay Rays":
                                    while self.categories[index[1]] in prohibited_teams:
                                        self.categories[index] = random.choice(self.choices)
                                case "New York Mets":
                                    while self.categories[index[1]] in prohibited_teams:
                                        self.categories[index] = random.choice(self.choices)
                                case "Arizona Diamondbacks":
                                    while self.categories[index[1]] in prohibited_teams:
                                        self.categories[index] = random.choice(self.choices)
                                case _:
                                    continue
                    case "ROY":
                        prohibited_teams = ["Arizona Diamondbacks", "San Diego Padres"]
                        for item in self.__get_grid_opposers(self.categories, index):
                            match(item[1]):
                                case "Arizona Diamondbacks":
                                    while self.categories[index[1]] in prohibited_teams:
                                        self.categories[index] = random.choice(self.choices)
                                case "San Diego Padres":
                                    while self.categories[index[1]] in prohibited_teams:
                                        self.categories[index] = random.choice(self.choices)
                                case _:
                                    continue

    
    @staticmethod
    def get_matchups(categories: list[list[tuple]]) -> list[tuple]:
        teams_top, teams_left = (categories[0], categories[1])
        matchups = [(top[1], left[1]) for top in teams_top for left in teams_left]
        return matchups

    def __str__(self) -> str:
        return str(self.categories)