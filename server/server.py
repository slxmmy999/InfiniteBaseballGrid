from flask import Flask, request, jsonify
from flask_cors import CORS
from server.GameCategories import GameCategories
from server.BaseballData import BaseballData

app = Flask(__name__)

CORS(app, "https://www.infiniteimmaculategrid.com")

@app.route("/get_new_grid", methods=["GET"])
def get_new_grid():
    categories = GameCategories()
    return jsonify(categories.get_grid())

@app.route("/search_players", methods=["GET"])
def search_players():
    query = request.args.get("name")
    players = BaseballData.search_players(query)
    data = players
    if len(data) > 0:
        if len(data) > 5:
            data = data[:5]
        players = []
        for x in range(len(data)):
            players.append(data[x]["fullName"])
        return jsonify(players)
    return jsonify([])

@app.route("/validate_player", methods=["GET"])
def validate_player():
    query = request.args.get("name")
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    players = BaseballData.search_players(query)
    teams = BaseballData.get_player_teams(players[0])
    if teams:
        if team1 in teams and team2 in teams:
            picture = BaseballData.get_player_picture(players[0])
            name = players[0]["fullName"]
            print("correct")
            return jsonify({"picture": picture, "name": name})
    # return nothing
    print("incorrect")
    return jsonify({})

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)