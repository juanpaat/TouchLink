"""
PC Remote Control Server
Main entry point - starts the server and handles incoming connections
"""

import socket
import threading
import sys
from connection import ConnectionHandler
from controller import Controller

class RemoteServer:
    def __init__(self, host='0.0.0.0', port=5555):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        self.controller = Controller()
        
    def get_local_ip(self):
        """Get the local IP address of this machine"""
        try:
            # Create a socket to determine local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception:
            return "127.0.0.1"
    
    def start(self):
        """Start the server and listen for connections"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            
            local_ip = self.get_local_ip()
            print("=" * 50)
            print("PC Remote Control Server Started")
            print("=" * 50)
            print(f"Server IP: {local_ip}")
            print(f"Port: {self.port}")
            print("\nWaiting for Android device to connect...")
            print("Enter this IP in your Android app to connect")
            print("\nPress Ctrl+C to stop the server")
            print("=" * 50)
            
            while self.running:
                try:
                    # Accept incoming connection
                    client_socket, address = self.server_socket.accept()
                    print(f"\n[+] Connection from {address[0]}:{address[1]}")
                    
                    # Handle client in a new thread
                    handler = ConnectionHandler(client_socket, address, self.controller)
                    client_thread = threading.Thread(target=handler.handle, daemon=True)
                    client_thread.start()
                    
                except KeyboardInterrupt:
                    print("\n\nShutting down server...")
                    break
                except Exception as e:
                    if self.running:
                        print(f"[!] Error accepting connection: {e}")
                    
        except Exception as e:
            print(f"[!] Failed to start server: {e}")
            sys.exit(1)
        finally:
            self.stop()
    
    def stop(self):
        """Stop the server and clean up"""
        self.running = False
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass
        print("Server stopped.")

if __name__ == "__main__":
    # Default port, can be changed
    PORT = 5555
    
    # Check for custom port argument
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 5555")
    
    server = RemoteServer(port=PORT)
    
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServer interrupted by user")
        sys.exit(0)
