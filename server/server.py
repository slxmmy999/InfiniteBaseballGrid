from flask import Flask, request, jsonify
from GameCategories import GameCategories

app = Flask(__name__)

@app.route("/get_new_grid", methods=["GET"])
def get_new_grid():
    categories = GameCategories()
    return jsonify(categories.get_grid())

if __name__ == '__main__':
    app.run(debug=True)