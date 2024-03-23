# pong-cli.py
import sys
import requests
import time

def start_game(pong_time_ms):
    try:
        response = requests.get(f"http://localhost:5000/start/{pong_time_ms}")
        if response.status_code == 200:
            print("Game started successfully.")
        else:
            print("Failed to start the game.")
    except requests.RequestException as e:
        print(f"Error starting the game: {e}")

def pause_game():
    try:
        response = requests.get("http://localhost:5000/pause")
        if response.status_code == 200:
            print("Game paused.")
        else:
            print("Failed to pause the game.")
    except requests.RequestException as e:
        print(f"Error pausing the game: {e}")

def stop_game():
    try:
        response = requests.get("http://localhost:5000/stop")
        if response.status_code == 200:
            print("Game stopped.")
        else:
            print("Failed to stop the game.")
    except requests.RequestException as e:
        print(f"Error stopping the game: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python pong-cli.py <command> [pong_time_ms]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'start':
        if len(sys.argv) != 3:
            print("Usage: python pong-cli.py start <pong_time_ms>")
            sys.exit(1)
        pong_time_ms = int(sys.argv[2])
        start_game(pong_time_ms)
    elif command == 'pause':
        pause_game()
    elif command == 'stop':
        stop_game()
    else:
        print("Invalid command. Available commands: start, pause, stop")
