import json
import os
import requests
from flask import Flask, jsonify, make_response

from dotenv import load_dotenv

load_dotenv()
print(os.getenv('API_KEY'))

app = Flask(__name__)

PORT = 3202
HOST = 'localhost'


@app.route("/parkings", methods=['GET'])
def get_parkings():
    parkings = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_parkings-publics-nantes-disponibilites/records?apikey={os.getenv('API_KEY')}")
    res = make_response(parkings.json(), 200)
    return res


if __name__ == "__main__":
    print("Server running in port %s" % PORT)
    app.run(host=HOST, port=PORT)