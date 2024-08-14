from BaseballData import BaseballData

class StatData():
    @staticmethod
    def verify_300_avg(player, team) -> bool:
        if player["stats"]:
            for item in player["stats"]:
                if item["type"]["displayName"] == "yearByYear":
                    for season in item["splits"]:
                        try:
                            if season["stat"]["battingAvg"] >= .300:
                                if season["team"]["name"] == team:
                                    return True
                        except KeyError:
                            continue
        return False