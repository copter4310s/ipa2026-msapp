from database import insert_router_interfaces
from get_interfaces import get_interfaces
import os
import time, pika, json

def get_message():
    host = "rabbitmq"
    credentials = pika.PlainCredentials('admin', 'rabbitmq')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host, 5672, "/", credentials))
    channel = connection.channel()
    data = None
    
    method_frame, header_frame, body = channel.basic_get('router_jobs')
    if method_frame:
        data = json.loads(body)
        channel.basic_ack(method_frame.delivery_tag)

    connection.close()
    print(data)
    return data

def worker():
    INTERVAL = 3.0
    next_run = time.monotonic()
    count = 0
    
    time.sleep(7)
    
    while True:
        now = time.time()
        now_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
        ms = int((now % 1) * 1000)  
        now_str_with_ms = f"{now_str}.{ms:03d}"
        print(f"[{now_str_with_ms}] run #{count}")

        data = get_message()
        if data:
            insert_router_interfaces(data["ip"], get_interfaces(data["ip"], data["username"], data["password"]))
        
        next_run += INTERVAL
        time.sleep(max(0.0, next_run - time.monotonic()))

if __name__=='__main__':
    worker()
