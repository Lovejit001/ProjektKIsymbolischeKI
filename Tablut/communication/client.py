#!/usr/bin/env python3
"""
Einfacher Client für den gspy Gameserver.
Führt nur den Handshake durch und erwartet ein "ok".
"""

import socket
import sys
import time
import argparse
from src import config
from src import makeMove
from src import debug
from src import alphaBeta
from src import checkBoard




#Lobby konfigurieren
#Optionen: tictactoe, archimedes, tablut
GAMETYPE = "tablut"

#Optionen: random, classic_tournament, double_tournament, round_robin
SCHEDULER = "random"

MIN_PLYERS = 2
MAX_PLYERS = 2
GAMEOVER = False

B = 'B'
W = 'W'
K = 'K'

starting_board = [
    [0, 0, 0, B, B, B, 0, 0, 0],
    [0, 0, 0, 0, B, 0, 0, 0, 0],
    [0, 0, 0, 0, W, 0, 0, 0, 0],
    [B, 0, 0, 0, W, 0, 0, 0, B],
    [B, B, W, W, K, W, W, B, B],
    [B, 0, 0, 0, W, 0, 0, 0, B],
    [0, 0, 0, 0, W, 0, 0, 0, 0],
    [0, 0, 0, 0, B, 0, 0, 0, 0],
    [0, 0, 0, B, B, B, 0, 0, 0]
]


parser = argparse.ArgumentParser(description="Beinhaltet Lobbyname, falls dieser nicht existiert wird eins erstellt.")
parser.add_argument('lobbyname', metavar='lobbyname',type = str, help="Wähle lobby die erstellt oder beigetreten werden soll")
args = parser.parse_args() 


def joinLobby(client):
    #Lobby beitreten/erstellen
    client.send(f"join {args.lobbyname}\n")
    #command =f"join {args.lobbyname}\n"
    #client.sendall(command.encode("utf-8"))
    response = client.recv()          
    print(f"Erfolgreich in {args.lobbyname} drin")  

def getGameData(client):

    res = client.recv()
    print(f"Empfangen: {res}")
    if res == "config":
        #Sammeln der Spieleinstellungen
        gameType = client.recv()
        print("1")
        print(gameType)
        timeAcc = client.recv()
        print("2")
        print(timeAcc)
        response = client.recv()
        print("3")
        print(response)
        board = client.recv()
        print("4")
        print(board)        
        verify = client.recv()
        print("5")
        print(verify)

    return gameType,timeAcc,response,board,verify

def createLobby(client):
    print("LOBBY ERSTELLEN:")
    client.send(f"create {args.lobbyname}\n")
    #command =f"create {args.lobbyname}\n"
    #client.sendall(command.encode("utf-8"))
    #response = client.recv(1024).decode("utf-8").strip()            
    response = client.recv()            

    print("TABLUT EINSTELLEN:")
    client.send(f"set game.type {GAMETYPE}\n")
    #command =f"set game.type {GAMETYPE}\n"
    #client.sendall(command.encode("utf-8"))
    #response = client.recv(1024).decode("utf-8").strip()
    response = client.recv()

    print("SCHEDULER EINSTELLEN:")       
    client.send(f"set scheduler {SCHEDULER}\n")
    #command =f"set scheduler {SCHEDULER}\n"
    #client.sendall(command.encode("utf-8"))
    #response = client.recv(1024).decode("utf-8").strip()
    response = client.recv()
    #print(response)

    print("MIN_PLAYERS EINSTELLEN:")       
    client.send(f"set min_players {MIN_PLYERS}\n")
    #command =f"set min_players {MIN_PLYERS}\n"
    #client.sendall(command.encode("utf-8"))
    #response = client.recv(1024).decode("utf-8").strip()
    response = client.recv()

    print("MAX_PLAYERS EINSTELLEN:")       
    client.send(f"set max_players {MAX_PLYERS}\n")
    #command =f"set max_players {MAX_PLYERS}\n"
    #client.sendall(command.encode("utf-8"))
    #response = client.recv(1024).decode("utf-8").strip()
    response = client.recv()


def registerLogin(client):
    #registrieren
    #command = "register\n"
    #client.sendall(command.encode("utf-8")) 
    #print(f"gesendet: {command}")
    # Antwort empfangen
    client.send("register\n")
    response = client.recv()
    client.send(f"login {response}\n")
    response = client.recv()             
    
    #print(f"Empfangen: {response}")   
    #login
    #command = f"login {response}\n"
    #client.sendall(command.encode("utf-8"))       
    #print(f"gesendet: {command}")  
    #response = client.recv(1024).decode("utf-8").strip()            
    #print(f"Empfangen: {response}")

def findLobbies(client):
    #command =f"ls\n"
    #client.sendall(command.encode("utf-8"))
    #print(f"gesendet: {command}")  
    client.send(f"ls\n")
    response = client.recv()            
    return response

def convertTo2D(boardStr):
    board = [[0 for _ in range(9)] for _ in range(9)]
    x= 0 
    y= 0
    counter = 0
    for val in boardStr:
        if not (val == " "): 
            if val == 'B' or val == 'W' or val == 'K' :
                board[x][y] = val
            else:
                board[x][y] = 0
            
            counter += 1
            if counter % 10 == 0:
                x += 1
                y = 0

def convertTo2D(board_Str):
    pieces = {'B','W','K'}
    if board_Str == '':
        board = starting_board
    else:
        board=  [
            [cell if cell in pieces else 0 for cell in row.split()]
            for row in board_Str.strip().slitlines()
        ]
    
    return board

def encode_move(bestmove):

    (startPos), (goalPos) = bestmove
    
    return f"move {startPos[0]},{startPos[1]},{goalPos[0]},{goalPos[1]}"

#TODO: man erhält "move A, B, C, D" => ((A,B),(C,D)) 
def decode_move(command):
    part = command.split()
    zahlen = part[1].split(",")

    a = int(zahlen[0])
    b = int(zahlen[1])
    c = int(zahlen[2])
    d = int(zahlen[3])

    return ((a,b),(c,d))


def myTurn(board,client):
    alphaBeta.getBestMove(board,config.onTurn,depth=3)
    makeMove.updateBoard(board,config.bestMove)
    convert_move=encode_move(config.bestMove)
    command =f"{convert_move}\n"
    print("MOVE IST:")
    print(command)
    print("AKTUELLES BOARD:")
    debug.print_board(board)
    client.send(f"{convert_move}\n")
    #client.sendall(command.encode("utf-8"))
    #TODO NACH JEDEM MOVE ERHÄLT MAN SEINE RESTLICHE ZEIT MIT !

    

def enemyTurn(board,response):
    print(f"MOVE VOM GEGNER: {response}")
    getMove = decode_move(response)      
    print(f"getMove VOM GEGNER: {getMove}")          
    makeMove.updateBoard(board,getMove)
    #switchTurn()

def switchTurn(onTurnFlag,player):
    if player == 'a' and onTurnFlag:
        config.onTurn = 'Black'
    elif player == 'a' and not onTurnFlag:
        config.onTurn = 'White'
    elif player == 'd' and onTurnFlag:
        config.onTurn = 'White'
    elif player == 'd' and not onTurnFlag :
        config.onTurn = 'Black' 


class Client:
    def __init__(self, client):
        self.client = client #UNKLAR
        self._writer = client.makefile('w', encoding='utf-8')
        self._reader = client.makefile('r', encoding='utf-8')
      
    def send(self, msg):
        print(msg)
        self._writer.write(msg)
        self._writer.flush()

    def recv(self) -> str:
        response = self._reader.readline().strip()
        print(f"Empfangen: {response}")
        return response
    
    def close(self):
        self.reader.close()
        self.writer.close()
        self.sock.close()



def main():
    LOBBYCREATOR = False
    # Server-Konfiguration (Standard-Werte anpassen falls nötig)
    HOST = "127.0.0.1"  # localhost
    PORT = 5000        # Standard-Port (ggf. anpassen)
    client = None

    try:
        # Verbindung zum Server herstellen
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        print(f"Verbunden mit {HOST}:{PORT}")
        
        client = Client(sock)
    
    
        client.send("gspy\n")
        response = client.recv()


        # Prüfen ob Antwort "ok" ist
        if response == "ok":
            print("✓ Handshake erfolgreich! Server hat 'ok' gesendet.")
            #TODO HIER SCHEIN NEN BUCK ZU SEIN
            registerLogin(client)  
            currentLobbies = findLobbies(client)

            if f"{args.lobbyname}" in currentLobbies:
                #Lobby beitreten:
                joinLobby(client)   
            #Falls Lobby nicht gefunden wird, muss man diese Lobby erstellen
            else:
                LOBBYCREATOR = True
                createLobby(client)

            if LOBBYCREATOR :
                #Creator versucht alle 3 sek Spiel zu starten, denn es kann sein das er alleine in Lobby ist, sonst spielbeginnt
                while True:
                    client.send(f"start\n")
                    response = client.recv()
                    #command = f"start\n"
                    #client.sendall(command.encode("utf-8"))
                    #response = client.recv(1024).decode("utf-8").strip()
                    #print(response)
                    if response == "queued":                        
                        break
                    time.sleep(3)

            else:
                print("Warte auf Spielstart...")
                while True:                    
                    #Es wird aus schleife rausgebrochen sobald Lobby ersteller "start drückt", Teilnehmer kriegt die Info queued.
                    #response = client.recv(1024).decode("utf-8").strip()
                    response = client.recv()
                    if response == "queued":
                        break
                    time.sleep(20)
            print("Spielbeginnt:")   

            #TODO timeAcc,PlayerTimAccount noch anpassen
            #TODO String FEN übers Terminal anpassbar
            #response = client.recv(1024).decode("utf-8").strip()

            gameType,timeAcc,playerTimeAccount,boardStr,verify = getGameData(client)

            print("A")
            board, onturn = debug.FenToBoard(boardStr.split("'")[1])
            print("B")
            debug.print_board(board)
            print("C")

            if gameType.split(" ")[2] != 'tablut':
                print(f"Falsches Spiel erhalten: {gameType}. Programm wird beendet.")
                sys.exit(1)

            if verify == 'ok':
                client.send(f"ok\n")
            
            response = client.recv()

            if response == "start":                
                print("START")
                switchTurn(True,onturn)
                print(config.onTurn)
                myTurn(board,client)

            elif response == "wait":
                print("Wait")
                switchTurn(False,onturn)
                print(config.onTurn)
                response = client.recv()                
                enemyTurn(board,response)
                myTurn(board,client)
            else:
                print(f"FEHLER Response war: {response}")
            
            response = client.recv()
    
            while True:
                
                #Spielende erreicht:
                response = client.recv()
                if response == 'over':
                    print(f"response: {response}")
                    break
                elif response == "err 'invalid move or not your turn'":... #TODO
                elif response == "err 'time account exceeded": ... #TODO
                elif response.startswith("move "): #Hier macht gegner Move 
                    #Move beim aktuellen Board updaten
                    enemyTurn(board,response)
                    #Move aussuchen und Server informieren
                    myTurn(board,client)
                else:
                    print(f"HIER NICHT BEACHTET COMMAND : {response}")

            print("GAME OVER")
            print("End Board: \n")
            debug.print_board(board)

            #TODO letzter Move wird nicht ausgeführt daher DRAW
            result = checkBoard.checkBoard2(board)
            if result == 2: 
                print("WINNER IS WHITE")
            elif result == -1:
                print("WINNER IS BLACK")
            else: 
                print("DRAW")

        else:
            print(f"✗ Unerwartete Antwort: {response}")


    except ConnectionRefusedError:
        print(f"Fehler: Konnte keine Verbindung zu {HOST}:{PORT} herstellen.")
        print("Stelle sicher, dass der gspy-Server läuft (Befehl: gameserver)")
        sys.exit(1)
    except Exception as e:
        print(f"Fehler: {e}")
        sys.exit(1)
    finally:
        client.close()
        print("Verbindung geschlossen.")



if __name__ == "__main__":
    main()