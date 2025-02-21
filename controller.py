# (running on controlling computer)
from tkinter import Label, Tk, Button
import socket
from time import sleep


ip_address = "192.168.1.104" # pi's ip
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 65432  
s.connect((ip_address, PORT))

root = Tk()
root.title("PiRover controller 1.0")
root.geometry("300x300")

def handle_keypress(event):
    s.sendall(event.keysym.encode('utf-8'))

l = Label(root, text="Use WASD to control the rover")
l.pack()

root.bind("<KeyRelease>", handle_keypress)
root.mainloop()
