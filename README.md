# python_keylogger
# Keylogger Collection

This repository contains different types of keyloggers developed using Python with the `pynput` library.

## Keyloggers Overview

### 1. Simple Keylogger:

**Description:** 
- Records keystrokes and logs them into `processmanager.txt`.
- Handles basic keys such as backspace, enter, shift, space, caps lock, and control.

**Usage:**
- Install the required dependencies:
  ```bash
  pip install pynput
- Run the program:
  ```bash
  python keylogger_1.py

### 2. Upgraded Keylogger:

**Description:** 
- Enhanced version that logs keystrokes to output.txt using the logging module.
- Supports additional special keys and provides more structured logging.

**Usage:**
- Install the required dependencies:
  ```bash
  python keylogger2_keylogger.py


### 3. NetKeylogger:

**Description:** 
- Consists of two parts: key_sender.py (client) and key_listener.py (server).
- key_sender.py sends keystrokes to a specified IP address and port.
- key_listener.py listens for keystrokes and prints them.

**Usage:**
- Run this on victim's machine to send the keystrokes to our remote machine:
  ```bash
  python key_listener.py

- Run this on our remote machine where we will receive the keystrokes sent by the victim's machine:
  ```bash
  python key_sender.py
  
### Installation:
**1. Clone the Repository:**
  ```bash
    git clone https://github.com/ShieldedDev/python_keylogger.git
  ```
    cd keylogger_collection

**2. Installing Dependencies:**
```
  pip install -r requirements.txt
```
