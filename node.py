import socket
import threading

class Node(threading.Thread):
    def __init__(self, node_id, server_address, server_port):
        super().__init__()
        self.node_id = node_id
        self.server_address = server_address
        self.server_port = server_port

    def run(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.server_address, self.server_port))
            print(f"Node {self.node_id} connected to the server on port {client_socket.getsockname()[1]}.")
        except ConnectionRefusedError:
            print(f"Node {self.node_id} failed to connect to the server.")
            return

        while True:
            message = input(f"Node {self.node_id}: Enter message to send: ")
            client_socket.sendall(message.encode('utf-8'))

        client_socket.close()
