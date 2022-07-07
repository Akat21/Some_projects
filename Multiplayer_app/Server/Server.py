import socket
from _thread import *
import sys
from Player import Player
import pickle
########INIT###########
server = "192.168.1.14"
port = 5555 ######ogarnij ktore mozna uzywac

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)
#######################


s.listen(2) ###LICZBA OSOB KTRA SIE MOZE POLACZYC
print("Waiting for connection, RDY")

players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,255,0))]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048*1))######Liczba odebranych info
            players[player] = data

            if not data:
                print("disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received",reply)
                print("Sending",reply)
            conn.sendall(pickle.dumps(reply))#########WYSLIJ
        except:
            break
    print("Lost Connectio")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept() ###AKCEPTUJE CONNECTION (CONN - what is connected, addr - IP)
    print("Connected to:",addr)

    start_new_thread(threaded_client,(conn, currentPlayer))
    currentPlayer += 1