"""
CAREFlow AI - Application Launcher
Starts the FastAPI server with auto-port detection and database initialization.
"""

import sys
import os
import socket
import uvicorn

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

from seed_data import seed_database
from database import DB_PATH

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def find_available_port(start_port: int = 8080) -> int:
    port = start_port
    while is_port_in_use(port) and port < 8100:
        port += 1
    return port

if __name__ == "__main__":
    # Check if database exists
    if not os.path.exists(DB_PATH):
        print("Database not found. Initializing seed records...")
        seed_database()
    
    port = 8080
    if is_port_in_use(port):
        # If running instance is already responding, inform user
        print(f"Note: Port {port} is active. If server is already running, access at: http://127.0.0.1:{port}")
    
    print("=" * 60)
    print("  CAREFlow AI - Intelligent Patient Care Agent")
    print(f"  Live Server: http://127.0.0.1:{port}")
    print("=" * 60)
    
    uvicorn.run("backend.app:app", host="127.0.0.1", port=port, reload=True)
