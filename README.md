# Python Chat Application

This is a simple yet effective client-server chat application built using Python's `socket` and `threading` modules. The project demonstrates real-time messaging between multiple clients connected to a server.

## Features
- Multi-client support for group chatting
- Uses threading to manage multiple connections
- Color-coded messages for improved readability
- User-friendly interface with timestamped messages
- Lightweight and easy to set up

## Requirements
Ensure you have Python installed along with the required dependencies:

```bash
pip install colorama
```

## Project Structure
```
.
├── client.py    # Client-side script for sending and receiving messages
├── main.py      # Server-side script for managing client connections
```

## How to Use

### 1. Start the Server
Run the `main.py` script and specify the server's IP address and port:

```bash
python main.py
```

### 2. Connect Clients
Run the `client.py` script for each client:

```bash
python client.py
```

You'll be prompted to enter your name before joining the chat.

### 3. Sending Messages
- Type your message and press **Enter** to send.
- Type `q` to quit the chat.

## How It Works
- The **server** (`main.py`) listens for incoming connections and starts a new thread for each connected client.
- The **client** (`client.py`) connects to the server and sends messages in real time.
- Messages are color-coded for clarity and include a timestamp for reference.
- The server efficiently broadcasts received messages to all connected clients.

## Example Usage
**Server Output:**
```
[*] Listening as 127.0.0.1:5002
[+] ('192.168.1.10', 45000) connected.
```

**Client Output:**
```
Enter your name: Alice
[*] Connecting to 127.0.0.1:5002...
[+] Connected.
```

**Sample Message:**
```
[2025-03-17 14:00:00] Alice: Hello, everyone!
```

## License
This project is licensed under the MIT License.

## Author
**IBRAHEMMA05**

---

