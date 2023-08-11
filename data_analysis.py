from server.Database import Database
from pymongo import MongoClient

class DataAnalysis:
    def __init__(self):
        self.db: Database = Database(MongoClient("mongodb+srv://samcoan100:sEWKVSSxhfmENclF@infinite-immaculate-gri.jnwda2y.mongodb.net/?retryWrites=true&w=majority"), False)

    def get_top_and_bottom(self):
        # Get the entire matchup collection and find the most picked and least picked answer for each document
        matchups = self.db.collection.find()
        for matchup in matchups:
            with open("data.txt", "w") as file:
                file.write(f"{Database.unnormalize_team_names(matchup['team_combination'])}\n")
                file.write(f"Most picked: {max(matchup['players'], key=lambda x: matchup['players'][x]['pick_frequency'])}\n")
                file.write(f"Least picked: {min(matchup['players'], key=lambda x: matchup['players'][x]['pick_frequency'])}\n\n")
                

da = DataAnalysis()
da.get_top_and_bottom()