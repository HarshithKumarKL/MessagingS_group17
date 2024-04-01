**MessagingS_group17**
*Messaging Application README*

Overview:
Using TCP/IP sockets, the Python application The Messaging Application emulates a messaging server. It enables several nodes, or clients, to connect to a server and exchange messages with one another via the server. By sending messages between nodes, the server enables inter-node communication.

Features:
1. Creates worker threads and a server object to manage client connections and communication.
2. Upon startup, nodes establish a connection with the server, which facilitates their communication with one another.
3. To track which ports are linked to which clients, the server keeps a table updated.
4. Manages simultaneous communication across numerous nodes.
5. Facilitates effortless communication from two to 255 nodes.


Files:
The project consists of the following files:
1. server.py: Contains the Server class, which implements the server functionality.
2. node.py: Contains the Node class, representing the client nodes that connect to the server.
3. main.py: The main script to run the application. It instantiates the server and nodes and manages their interaction.

Usage:
To run the Messaging Application, follow these steps:
1. Clone the repository to your local machine:
    git clone <repository_url>
2. Navigate to the project directory:
    cd messaging_app
3.Run the main script with the desired number of nodes (2 to 255):
    python3 main.py <number_of_nodes>
4. Follow the prompts to interact with the nodes. Nodes can send messages to each other via the server.
5. Press Ctrl + C to stop the application when done. This will shut down all nodes and the server cleanly.
   
Dependencies:
Installing Python 3.x on your computer is necessary for using the Messaging Application. Please feel free to contribute to the project! Feel free to start an issue or send a pull request on GitHub if you have any improvements, bug corrections, or ideas. Permission to use Under the MIT License, this project is permitted.
