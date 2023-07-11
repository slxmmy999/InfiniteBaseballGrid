from flask import Flask, request, jsonify
from flask_cors import CORS
from GameCategories import GameCategories

app = Flask(__name__)

CORS(app, resources={r"/get_new_grid": {"origins": "http://localhost:3000"}})

@app.route("/get_new_grid", methods=["GET"])
def get_new_grid():
    categories = GameCategories()
    return jsonify(categories.get_grid())

if __name__ == '__main__':
    app.run(debug=True)