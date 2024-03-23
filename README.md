# MessagingS_group17
Messaging Application README
Overview

The Messaging Application is a Python program that simulates a messaging server using TCP/IP sockets. It allows multiple nodes (clients) to connect to a server and communicate with each other through the server. The server facilitates inter-node communication by forwarding messages between nodes.

Features

Spawns a server object and worker threads to handle client connections and communication.
Nodes connect to the server upon startup and communicate with each other via the server.
The server maintains a table to keep track of which ports have which clients connected to them.
Handles communication between multiple nodes simultaneously.
Enables communication between 2 to 255 nodes easily.
Files
The project consists of the following files:

server.py: Contains the Server class, which implements the server functionality.
node.py: Contains the Node class, representing the client nodes that connect to the server.
main.py: The main script to run the application. It instantiates the server and nodes and manages their interaction.

Usage

To run the Messaging Application, follow these steps:

Clone the repository to your local machine:

git clone <repository_url>
Navigate to the project directory:

cd messaging_app
Run the main script with the desired number of nodes (2 to 255):

python3 main.py <number_of_nodes>
Follow the prompts to interact with the nodes. Nodes can send messages to each other via the server.

Press Ctrl + C to stop the application when done. This will shut down all nodes and the server cleanly.

Dependencies
The Messaging Application requires Python 3.x to be installed on your system.

Contributions
Contributions to the project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request on GitHub.

License
This project is licensed under the MIT License.


