import json
import os
from datetime import datetime, date

import requests
from flask import Flask, jsonify, make_response, render_template, request, send_from_directory, redirect, url_for
from flask_cors import CORS
from urllib.parse import quote
from dotenv import load_dotenv

app = Flask(__name__)
cors = CORS(app)
PORT = 5000
HOST = '0.0.0.0'
    
@app.route("/api/listactivities", methods=['GET'])
def get_all_activites():
    activites = requests.get("https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?limit=100")
    res = make_response(activites.json(), 200)
    return res

@app.route("/api/freeactivities", methods=['GET'])
def get_free_activites():
    activites = requests.get("https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?limit=100&where=gratuit%3D%20%22oui%22")
    res = make_response(activites.json(), 200)
    return res

@app.route("/api/activity/<id>", methods=['GET'])
def get_activity_by_id(id):
    activity = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?limit=100&where=id_manif%3D%20{id}")
    res = make_response(activity.json(), 200)
    return res

@app.route("/api/activitiesbydate/<date>", methods=['GET'])
def get_activities_by_date(date):
    date_obj = datetime.strptime(date, "%Y%m%d")
    date_formatee = date_obj.strftime("%Y-%m-%d")
    activity = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?limit=100&where=date%3Ddate'{date_formatee}'")
    res = make_response(activity.json(), 200)
    return res

@app.route("/api/todayactivities", methods=['GET'])
def get_today_activities():
    date_obj = date.today()
    date_formatee = date_obj.strftime("%Y%m%d")
    return get_activities_by_date(date_formatee)

@app.route("/api/activity/<id>/<date>", methods=['GET'])
def get_activity_by_id_date(id, date):
    date_obj = datetime.strptime(date, "%Y%m%d")
    date_formatee = date_obj.strftime("%Y-%m-%d")
    activity = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?limit=100&where=id_manif%3D%20{id}%20and%20date%3Ddate'{date_formatee}'")
    res = make_response(activity.json(), 200)
    return res

@app.route("/api/categories", methods=['POST'])
def get_categories_filter():
    data = request.json
    categories_list = data.get('categories_list', [])

    filter = ''
    for i in categories_list:
        encoded_category = quote(i)
        if filter != '' :
            filter += f"%20or%20"
        filter += f"categorie_1%3D%20%22{encoded_category}%22%20or%20categorie_2%20%3D%20%22{encoded_category}%22%20or%20categorie_3%20%3D%20%22{encoded_category}%22%20or%20categorie_4%20%3D%20%22{encoded_category}%22%20or%20categorie_5%20%3D%20%22{encoded_category}%22"
    
    categories = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?limit=100&where={filter}")
    
    res = make_response(categories.json(), 200)
    return res


@app.route("/api/allcategories", methods=['GET'])
def get_all_categories():
    all_categories = {'results': {'categories':[]}}
    categories_1 = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?select=categorie_1&group_by=categorie_1&limit=100").json()
    categories_2 = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?select=categorie_2&group_by=categorie_2&limit=100").json()
    categories_3 = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?select=categorie_3&group_by=categorie_3&limit=100").json()
    categories_4 = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?select=categorie_4&group_by=categorie_4&limit=100").json()
    categories_5 = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-evenements-nantes-nantes-metropole/records?select=categorie_5&group_by=categorie_5&limit=100").json()

    all_categories["results"]["categories"] = list(map(lambda result: result["categorie_1"], categories_1["results"]))
    all_categories["results"]["categories"] += list(map(lambda result: result["categorie_2"], list(filter(lambda result: not result["categorie_2"] in all_categories["results"]["categories"], categories_2["results"]))))
    all_categories["results"]["categories"] += list(map(lambda result: result["categorie_3"], list(filter(lambda result: not result["categorie_3"] in all_categories["results"]["categories"], categories_3["results"]))))
    all_categories["results"]["categories"] += list(map(lambda result: result["categorie_4"], list(filter(lambda result: not result["categorie_4"] in all_categories["results"]["categories"], categories_4["results"]))))
    all_categories["results"]["categories"] += list(map(lambda result: result["categorie_5"], list(filter(lambda result: not result["categorie_5"] in all_categories["results"]["categories"], categories_5["results"]))))

    all_categories["results"]["categories"] = list(filter(None, all_categories["results"]["categories"]))
    res = make_response(all_categories, 200)
    return res

if __name__ == "__main__":
    print("Server running in port %s" % PORT)
    app.run(host=HOST, port=PORT)
