class Database:
    def __init__(self, mongo_client, dev: bool):
        # Initialize the class with a MongoClient object 
        self.client = mongo_client
        self.db = self.client["infinite-immaculate-grid"]
        # Set the database to the dev database if dev is True, otherwise set it to the prod database (in order to avoid overwriting the prod database because I'm a dumbass)
        if dev:
            self.collection = self.db["dev"]
        else:
            self.collection = self.db["matchup-statistics"]
    
    def __normalize_team_names(teams: tuple[str, str]) -> str:
        return teams[0].lower().replace(" ", "") + teams[0].lower().replace(" ", "")
    
    def __normalize_player_name(player: str) -> str:
        return player.lower().replace(" ", "")

    def __matchup(self, teams: tuple[str, str], player: str) -> str:
        template = {
            "team_combination": self.__normalize_team_names(teams),
            "total_picks": 1,
            "players": {
                self.__normalize_player_name(player): {
                    "pick_frequency": 1
                }
            }
        }
        return template
    
    # Query the MongoDB database to find the player if they exist in the team combination
    async def __find_player(self, teams: tuple[str, str], player: str):
        matchup = self.__normalize_team_names(teams)


    async def add_matchup(self, team1: str, team2: str, player: str):
        await self.collection.insert_one(self.__matchup((team1, team2), player))

