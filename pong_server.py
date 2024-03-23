# server.py
from flask import Flask, request
import threading
import requests
import time
import sys

app = Flask(__name__)

pong_time_ms = None
pong_paused = False
pong_stopped = False
instance_ip = None
instance_port = None

@app.route('/ping')
def ping():
    print("Received ping.")
    return 'pong', 200

@app.route('/start/<int:pong_time>')
def start(pong_time):
    global pong_time_ms
    pong_time_ms = pong_time
    threading.Thread(target=send_pong).start()
    return 'Game started.', 200

@app.route('/pause')
def pause():
    global pong_paused
    pong_paused = True
    return 'Game paused.', 200

@app.route('/resume')
def resume():
    global pong_paused
    pong_paused = False
    return 'Game resumed.', 200

@app.route('/stop')
def stop():
    global pong_stopped
    pong_stopped = True
    return 'Game stopped.', 200

def send_pong():
    global pong_time_ms, instance_ip, instance_port
    while not pong_stopped:
        try:
            print("Sending ping to the other server...")
            requests.get(f"http://{instance_ip}:{instance_port}/ping")
            time.sleep(pong_time_ms / 1000)
        except requests.RequestException as e:
            print(f"Error sending ping: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python server.py <instance_ip> <instance_port>")
        sys.exit(1)

    instance_ip = sys.argv[1]
    instance_port = int(sys.argv[2])
    print(f"Starting server on {instance_ip}:{instance_port}")
    app.run(host=instance_ip, port=instance_port)
