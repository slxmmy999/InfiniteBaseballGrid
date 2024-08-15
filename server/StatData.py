from BaseballData import BaseballData

class StatData():
    @staticmethod
    def verify_300_avg(player, team) -> bool:
        if player["stats"]:
            for item in player["stats"]:
                if item["type"]["displayName"] == "yearByYear":
                    for season in item["splits"]:
                        try:
                            if float(season["stat"]["avg"]) >= .300:
                                if season["team"]["name"] == team:
                                    return True
                        except KeyError:
                            continue
        return False
    
    @staticmethod
    def verify_40_hr(player, team) -> bool:
        if player["stats"]:
            for item in player["stats"]:
                if item["type"]["displayName"] == "yearByYear":
                    for season in item["splits"]:
                        try:
                            if season["stat"]["homeRuns"] >= 40:
                                if season["team"]["name"] == team:
                                    return True
                        except KeyError:
                            continue
        return False
    
    @staticmethod
    def verify_cy_young(player, team) -> bool:
        if player["awards"]:
            for award in player["awards"]:
                if "Cy Young" in award["name"]:
                    for word in team.split():
                        if word in award["team"]["teamName"]:
                            return True
                # print(award)
        return False
    
    @staticmethod
    def verify_mvp(player, team) -> bool:
        if player["awards"]:
            for award in player["awards"]:
                if "Most Valuable Player" in award["name"]:
                    for word in team.split():
                        print(word)
                        if word in award["team"]["teamName"]:
                            return True
                # print(award)
        return False
    