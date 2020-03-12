import tkinter as tk
# from tkinter import *
from tkinter import filedialog, Text
import os

root = tk.Tk()


apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempapps = f.read()
        tempapps = tempapps.split(',')
        apps = [x for x in tempapps if x.strip()]



def addApps():
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select Folder", filetypes = (("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "grey")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=550, width= 550, bg ="#263D42")
canvas.pack()

frame = tk.Frame(root,bg= "white")
frame.place(relheight=1, relwidth=0.8, relx=0.1, rely=0)

openfile = tk.Button(root, text="Open File", padx = 3, pady = 3 ,fg = "white", bg="#263D42", command = addApps)
openfile.pack()


runapps = tk.Button(root, text="Run Apps", padx = 3, pady = 3 ,fg = "white", bg="#263D42", command = runApps)
runapps.pack()

check = tk.Checkbutton(frame)
check.pack()

for app in apps:
    label = tk.Label(frame)
    label.pack()

root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')