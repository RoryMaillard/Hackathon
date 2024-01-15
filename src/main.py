import json
import os
import requests
from flask import Flask, jsonify, make_response, render_template, request, send_from_directory
from flask_cors import CORS
from urllib.parse import quote
from dotenv import load_dotenv

app = Flask(__name__)
cors = CORS(app)
PORT = 5001
HOST = '0.0.0.0'

@app.route('/')
def serve_static():
    return send_from_directory('./../dist', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('./../dist', filename)
    
@app.route("/listactivities", methods=['GET'])
def get_all_activites():
    activites = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=44&apikey={os.getenv('API_KEY')}")
    res = make_response(activites.json(), 200)
    return res

@app.route("/activity/<id>/<date>", methods=['GET'])
def get_activity_by_id_date(id, date):
    date_obj = datetime.strptime(date, "%Y%m%d")
    date_formatee = date_obj.strftime("%Y-%m-%d")
    activity = requests.get(
        f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=100&where=id_manif%3D%20%22{id}%22%20and%20date%3Ddate'{date_formatee}'&apikey={os.getenv('API_KEY')}")
    res = make_response(activity.json(), 200)
    return res

@app.route("/activity/<id>", methods=['GET'])
def get_activity_by_id(id):
    activity = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=100&where=id_manif%3D%20%22{id}%22&apikey={os.getenv('API_KEY')}")
    res = make_response(activity.json(), 200)
    return res

@app.route("/activities/<activity>", methods=['GET'])
def get_activites_filter(activity):
    encoded_activity = quote(activity)
    activites = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=100&where=nom%3D%20%22{encoded_activity}%22&apikey={os.getenv('API_KEY')}")
    res = make_response(activites.json(), 200)
    return res


@app.route("/categories", methods=['POST'])
def get_categories_filter():
    data = request.get_json()
    categories_list = data.get('categories_list', [])

    filter = ''
    for i in categories_list:
        encoded_category = quote(i)
        filter + f"categorie_1%3D%20%22{encoded_category}%22%20or%20categorie_2%20%3D%20%22{encoded_category}%22%20or%20categorie_3%20%3D%20%22{encoded_category}%22%20or%20categorie_4%20%3D%20%22{encoded_category}%22%20or%20categorie_5%20%3D%20%22{encoded_category}%22"

    categories = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=100&where={filter}&apikey={os.getenv('API_KEY')}")

    res = make_response(categories.json(), 200)
    return res


@app.route("/allcategories", methods=['GET'])
def get_all_categories():
    all_categories = {'results': {'categories':[]}}
    categories_1=requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_1&group_by=categorie_1&limit=100&apikey={os.getenv('API_KEY')}").json()
    categories_2=requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_2&group_by=categorie_2&limit=100&apikey={os.getenv('API_KEY')}").json()
    categories_3=requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_3&group_by=categorie_3&limit=100&apikey={os.getenv('API_KEY')}").json()
    categories_4=requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_4&group_by=categorie_4&limit=100&apikey={os.getenv('API_KEY')}").json()
    categories_5=requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?select=categorie_5&group_by=categorie_5&limit=100&apikey={os.getenv('API_KEY')}").json()
    for i in categories_1["results"]:
        if not (i["categorie_1"] in all_categories["results"]["categories"] or i["categorie_1"] == None):
            all_categories["results"]["categories"].append(i["categorie_1"])

    for i in categories_2["results"]:
        if not (i["categorie_2"] in all_categories["results"]["categories"] or i["categorie_2"] == None):
            all_categories["results"]["categories"].append(i["categorie_2"])

    for i in categories_3["results"]:
        if not (i["categorie_3"] in all_categories["results"]["categories"] or i["categorie_3"] == None):
            all_categories["results"]["categories"].append(i["categorie_3"])

    for i in categories_4["results"]:
        if not (i["categorie_4"] in all_categories["results"]["categories"] or i["categorie_4"] == None):
            all_categories["results"]["categories"].append(i["categorie_4"])

    for i in categories_5["results"]:
        if not (i["categorie_5"] in all_categories["results"]["categories"] or i["categorie_5"] == None):
            all_categories["results"]["categories"].append(i["categorie_5"])

    res = make_response(all_categories, 200)
    return res

if __name__ == "__main__":
    print("Server running in port %s" % PORT)
    app.run(host=HOST, port=PORT)
