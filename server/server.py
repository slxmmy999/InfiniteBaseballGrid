from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_new_grid", methods=["GET"])
def get_new_grid():
    