from StatData import StatData
from BaseballData import BaseballData

async def test_stats():
    player = await BaseballData.search_players("Mike Trout")
    pitcher = await BaseballData.search_players("Max Scherzer")

    print(player)

    team = "Los Angeles Angels"

    print(StatData.verify_300_avg(player[0], team))
    print(StatData.verify_40_hr(player[0], team))
    print(StatData.verify_cy_young(pitcher[0], team))
    print(StatData.verify_mvp(player[0], team))

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_stats())
