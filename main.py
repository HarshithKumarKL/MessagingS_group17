# main.py
import sys
import threading
from server import Server
from node import Node

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <number_of_nodes>")
        return
    
    num_nodes = int(sys.argv[1])

    server = Server()
    server_thread = threading.Thread(target=server.run)
    server_thread.start()

    nodes = []
    for i in range(1, num_nodes + 1):
        node = Node(i, "127.0.0.1", 8088)
        nodes.append(node)
        node.start()

    for node in nodes:
        node.join()

    server.stop()

if __name__ == "__main__":
    main()
