from server.Database import Database
from pymongo import MongoClient

class DataAnalysis:
    def __init__(self):
        self.db: Database = Database(MongoClient("mongodb+srv://samcoan100:sEWKVSSxhfmENclF@infinite-immaculate-gri.jnwda2y.mongodb.net/?retryWrites=true&w=majority"), False)

    @staticmethod
    def pick_frequency(player_name, players):
        try:
            return players[player_name]['pick_frequency']
        except KeyError:
            return 10  # or another value that makes sense in your context

    def get_top_and_bottom(self):
        # Get the entire matchup collection and find the most picked and least picked answer for each document
        matchups = self.db.collection.find()
        with open("full_data.txt", "w") as file:
            for matchup in matchups:
                file.write(f"{Database.unnormalize_team_names(matchup['team_combination'])}\n")
                for player in matchup['players']:
                    file.write(f"{player} | {self.pick_frequency(player, matchup['players'])}\n")
                file.write("\n")
                

da = DataAnalysis()
da.get_top_and_bottom()