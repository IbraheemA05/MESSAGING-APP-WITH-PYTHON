import socket
from threading import Thread

SERVER_HOST = input("Enter the IP address of the server: ").strip()
SERVER_PORT = int(input("Enter the port number of the server: ").strip())
SEPARATOR_TOKEN = "<SEP>"

client_sockets = set()

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")


def listen_for_client(cs):
    """
    This function keeps listening for a message from `cs` socket.
    Whenever a message is received, broadcast it to all other connected clients.
    """
    while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()
            if not msg:
                raise Exception("Client disconnected")
        except Exception as e:
            # client no longer connected
            # remove it from the set and close the socket
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
            cs.close()
            break
        else:
            # if we received a message, replace the <SEP> 
            # token with ": " for nice printing
            msg = msg.replace(SEPARATOR_TOKEN, ": ")
            # iterate over all connected sockets
            for client_socket in client_sockets:
                # and send the message
                client_socket.send(msg.encode())

while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
