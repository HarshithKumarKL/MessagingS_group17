import socket
import threading
from queue import Queue

class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8088
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients_table = {}  # Table to keep track of connected clients
        self.buffer_size = 1024
        self.frame_buffer = Queue()  # Global frame buffer (queue)
        self.lock = threading.Lock()  # Lock to ensure thread safety

    def run(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()

        print("Server initiated, listening to connections...")

        while True:
            try:
                client_socket, addr = self.server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, addr))
                client_thread.start()
            except Exception as e:
                print(f"Error occurred while accepting client connection: {e}")

    def handle_client(self, client_socket, addr):
        print(f"Connection established with {addr}")
        port = addr[1]
        self.clients_table[port] = client_socket

        while True:
            try:
                data = client_socket.recv(self.buffer_size)
                if not data:
                    print(f"Client with port {port} has disconnected.")
                    with self.lock:
                        del self.clients_table[port]
                    break
                print(f"Received from Client {port}: {data.decode('utf-8')}")
                
                
                
                # Forward data to other clients
                self.forward_data(port, data)
            except Exception as e:
                print(f"Error occurred with client {port}: {e}")

        client_socket.close()

    def forward_data(self, sender_port, message):
        with self.lock:
            for port, client_socket in self.clients_table.items():
                if port != sender_port:
                    try:
                        client_socket.sendall(message)
                    except Exception as e:
                        print(f"Error occurred while sending message to port {port}: {e}")

    def stop(self):
        self.server_socket.close()
