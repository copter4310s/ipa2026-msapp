from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from bson import ObjectId
from pymongo import MongoClient
import os

mongo_uri  = os.environ.get("MONGO_URI")
db_name    = os.environ.get("DB_NAME")

client = MongoClient(mongo_uri)
mydb = client[db_name]
mycol = mydb["routers"]
table_interfaces = mydb["interface_status"]

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", data=mycol.find())

@app.route("/add", methods=["POST"])
def add_router():
    ip = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")

    if ip and username and password:
        mycol.insert_one({ "ip": ip, "username": username, "password": password })
    return redirect(url_for("main"))

@app.route("/delete", methods=["POST"])
def delete_router():
    try:
        mycol.delete_one({"_id": ObjectId(request.form.get("id"))})
    except Exception:
        pass
    return redirect(url_for("main"))

@app.route("/router/<ip>", methods=["GET"])
def get_interface(ip):
    interface_list = table_interfaces.find({"router_ip": ip})
    render_data = {"ip": ip, "data": interface_list}

    return render_template("interfaces.html", data=render_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

