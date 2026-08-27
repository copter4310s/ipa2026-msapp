import os
import datetime
from pymongo import MongoClient

mongo_uri  = os.environ.get("MONGO_URI")
db_name    = os.environ.get("DB_NAME")

def insert_router_interfaces(router_ip, interfaces):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    table = db["interface_status"]
    table.insert_one({ "router_ip": router_ip, "timestamp": datetime.datetime.now(), "interfaces": interfaces })

if __name__=='__main__':
    insert_router_interfaces("172.31.67.99", [{'interface': 'GigabitEthernet0/0', 'ip_address': '172.31.67.11', 'status': 'up', 'proto': 'up'}, {'interface': 'GigabitEthernet0/1', 'ip_address': 'unassigned', 'status': 'administratively down', 'proto': 'down'}, {'interface': 'GigabitEthernet0/2', 'ip_address': 'unassigned', 'status': 'administratively down', 'proto': 'down'}, {'interface': 'GigabitEthernet0/3', 'ip_address': 'unassigned', 'status': 'administratively down', 'proto': 'down'}])