from quart import Quart, request, jsonify, Response
from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

database_connection_string = os.getenv("DB_CONNECTION_STRING")
dev_ip = os.getenv("DEV_IP")

dev = True
if dev:
    from GameCategories import GameCategories
    from BaseballData import BaseballData
    from Database import Database
else:
    from server.GameCategories import GameCategories
    from server.BaseballData import BaseballData
    from server.Database import Database
import datetime

mongo_client = AsyncIOMotorClient(database_connection_string)
db: Database = Database(mongo_client, dev)

app = Quart(__name__)

@app.after_request
async def after_request(response):
    if dev:
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response
    else:
        response.headers["Access-Control-Allow-Origin"] = "https://www.infiniteimmaculategrid.com"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response

@app.route("/get_new_grid", methods=["GET"])
async def get_new_grid():
    categories: GameCategories = GameCategories()
    return jsonify(categories.get_grid())

@app.route("/search_players", methods=["GET"])
async def search_players():
    query: str = request.args.get("name")
    players: list = await BaseballData.search_players(query)
    data: list = players
    if len(data) > 0:
        if len(data) > 5:
            data = data[:5]
        players: list = []
        for x in range(len(data)):
            start: str = ''
            end: str = ''
            try:
                if data[x]['active']:
                    start = data[x]['mlbDebutDate'][:4]
                    end = datetime.datetime.now().year
                else:
                    start = data[x]['mlbDebutDate'][:4]
                    end = data[x]['lastPlayedDate'][:4]
                players.append(data[x]["fullName"] + f" | ({start}-{end})")
            except KeyError:
                players.append(data[x]["fullName"])
        return jsonify(players)
    return jsonify([])

@app.route("/validate_player", methods=["GET"])
async def validate_player():
    query = request.args.get("name")
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    players = await BaseballData.search_players(query)
    player = ''
    for x in range(len(players)):
        if players[x]["fullName"] == query:
            player = players[x]
            break
    teams = BaseballData.get_player_teams(player)
    if teams:
        if team1 in teams and team2 in teams:
            picture = BaseballData.get_player_picture(player)
            name = player["fullName"]
            id = player['link'].split('/')[-1]
            await db.update_matchup(teams=(team1, team2), player=name, id=id)
            rarity_score = await db.calculate_rarity_score(teams=(team1, team2), player=name, id=id)
            return jsonify({"picture": picture, "name": name, "rarity_score": rarity_score})
    # return nothing
    return jsonify({})

@app.route("/set_shared_grid", methods=["POST"])
async def set_shared_grid():
    data = await request.get_json()
    grid = data["grid"]
    id = await db.set_shared_grid(grid)
    return jsonify({"id": id})

@app.route("/get_shared_grid", methods=["GET"])
async def get_shared_grid():
    id = request.args.get("id")
    grid = await db.get_shared_grid(id)
    if grid == []:
        return Response(status=404)
    return jsonify(grid)

@app.route("/get_top_players", methods=["POST"])
async def get_top_players():
    data = await request.get_json()
    grid = data["grid"]
    matchups = GameCategories.get_matchups(grid)
    top_players = []
    for matchup in matchups:
        top_players.append(await db.get_top_player(matchup))
    return jsonify(top_players)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)