#!/usr/bin/env python3
"""
Einfacher Client für den gspy Gameserver.
Führt nur den Handshake durch und erwartet ein "ok".
"""

import socket
import sys
import time
import argparse
import math
from Tablut.src.gamelogic import config
from Tablut.src.gamelogic import makeMove
from Tablut.src.gamelogic import debug
from Tablut.src.models import alphaBetaWithPVS
from Tablut.src.gamelogic import checkBoard


#Lobby konfigurieren:

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
    response = client.recv()          
    print(f"Erfolgreich in {args.lobbyname} drin")  

def getGameData(client):

    res = client.recv()
    print(f"Empfangen: {res}")
    if res == "config":
        #Sammeln der Spieleinstellungen
        gameType = client.recv()
        print(gameType)
        timeAcc = client.recv()
        print(timeAcc)
        response = client.recv()
        print(response)
        board = client.recv()
        print(board)        
        verify = client.recv()
        print(verify)

    return gameType,timeAcc,response,board,verify

def createLobby(client):
    print("LOBBY ERSTELLEN:")
    client.send(f"create {args.lobbyname}\n")       
    response = client.recv()            

    print("TABLUT EINSTELLEN:")
    client.send(f"set game.type {GAMETYPE}\n")
    response = client.recv()

    print("SCHEDULER EINSTELLEN:")       
    client.send(f"set scheduler {SCHEDULER}\n")
    response = client.recv()

    print("MIN_PLAYERS EINSTELLEN:")       
    client.send(f"set min_players {MIN_PLYERS}\n")
    response = client.recv()

    print("MAX_PLAYERS EINSTELLEN:")       
    client.send(f"set max_players {MAX_PLYERS}\n")


    #response = client.recv(1024).decode("utf-8").strip()
    response = client.recv()


def registerLogin(client):
    #registrieren
    # Antwort empfangen
    client.send("register\n")
    response = client.recv()
    client.send(f"login {response}\n")
    response = client.recv()             
    

def findLobbies(client):
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


def myTurn(board,client,time):
    alphaBetaWithPVS.iterative_deepening(board,config.onTurn,time)
    print(config.onTurn)
    convert_move=encode_move(config.bestMove)
    command =f"{convert_move}\n"
    print(f"MOVE IST: {config.bestMove}")
    print(command)
    print("AKTUELLES BOARD:")
    debug.print_board(board)
    print("GEUPDATES BOARD:")
    makeMove.updateBoard(board,config.bestMove)
    debug.print_board(board)
    client.send(f"{convert_move}\n")

    
def enemyTurn(board,response):
    print(f"MOVE VOM GEGNER: {response}")
    getMove = decode_move(response)      
    print(f"getMove VOM GEGNER: {getMove}")          
    makeMove.updateBoard(board,getMove)


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
        self._reader.close()
        self._writer.close()


def main():
    LOBBYCREATOR = False
    HOST = "bore.pub"

    PORT = 5000        # Standard-Port (ggf. anpassen)
    #PORT = 44843
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
            registerLogin(client)  
            currentLobbies = findLobbies(client)

            if f"{args.lobbyname}" in currentLobbies:
                #Lobby beitreten:
                joinLobby(client)   
            else:
                LOBBYCREATOR = True
                createLobby(client)
            if LOBBYCREATOR :
                #Creator versucht alle 3 sek Spiel zu starten, denn es kann sein das er alleine in Lobby ist, sonst spielbeginnt
                while True:
                    client.send(f"start\n")
                    response = client.recv()
                    if response == "queued":                        
                        break
                    time.sleep(3)
            
            else:
                print("Warte auf Spielstart...")
                while True:                    
                    #Es wird aus schleife rausgebrochen sobald Lobby ersteller "start drückt", Teilnehmer kriegt die Info queued.
                    response = client.recv()
                    if response == "queued":
                        break
                    time.sleep(20)
            print("Spielbeginnt:")   

            gameType,timeAcc,playerTimeAccount,boardStr,verify = getGameData(client)

            board, onturn = debug.FenToBoard(boardStr.split("'")[1])
            config.init_pieces(board)
            debug.print_board(board)

            if gameType.split(" ")[2] != 'tablut':
                print(f"Falsches Spiel erhalten: {gameType}. Programm wird beendet.")
                sys.exit(1)
            
            myTime = float(timeAcc.split()[-1])
            print(f"MYTIME IS : {myTime}")

            if verify == 'ok':
                client.send(f"ok\n")
            
            response = client.recv()

            if response == "start":                
                print("START")
                switchTurn(True,onturn)
                print(config.onTurn)
                myTurn(board,client,myTime)

            elif response == "wait":
                print("Wait")
                switchTurn(False,onturn)
                print(config.onTurn)
                response = client.recv()                
                enemyTurn(board,response)
                myTurn(board,client,myTime)
            else:
                print(f"FEHLER Response war: {response}")
            
            response = client.recv()
    
            while True:
                
                #Spielende erreicht:
                response = client.recv()
                if response == 'over':
                    print(f"response: {response}")
                    break
                elif response == "err 'invalid move or not your turn'":
                    print(response) 
                elif response == "err 'time account exceeded'":  

                    if config.onTurn == 'Black' :
                        result =1 
                    elif  config.onTurn == 'White' :
                        result = -1  
                elif response.startswith("move "): #Hier macht gegner Move 
                    #Move beim aktuellen Board updaten
                    enemyTurn(board,response)
                    #Move aussuchen und Server informieren
                    myTurn(board,client,myTime)
                elif response.startswith("time "):
                    myTime = float(response.split(" ")[1])
                    accTime = float(response.split(" ")[1])
                else:
                    print(f"NICHT BEACHTETER COMMAND : {response}")

            print("GAME OVER")
            print("End Board: \n")
            debug.print_board(board)
            result = checkBoard.checkBoard(board)

            if result != 1 and result != -1:
                result = checkBoard.checkBoard(board)

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