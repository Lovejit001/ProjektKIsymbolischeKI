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
    command =f"join {args.lobbyname}\n"
    client.sendall(command.encode("utf-8"))
    response = client.recv(1024).decode("utf-8").strip()          
    print(f"Empfangen: {response}")
    print(f"Erfolgreich in {args.lobbyname} drin")  

def getGameData(client,res):
    print(f"Empfangen: {res}")
    if res == "config":
        #Sammeln der Spieleinstellungen
        gameType = client.recv(1024).decode("utf-8").strip()
        print(gameType)
        timeAcc = client.recv(1024).decode("utf-8").strip()
        print(timeAcc)
        response = client.recv(1024).decode("utf-8").strip()
        print(response)
        board = client.recv(1024).decode("utf-8").strip()
        print(board)        
        verify = client.recv(1024).decode("utf-8").strip()
        print(verify)

    return gameType,timeAcc,response,board,verify

def createLobby(client):
    print("LOBBY ERSTELLEN:")
    command =f"create {args.lobbyname}\n"
    client.sendall(command.encode("utf-8"))
    response = client.recv(1024).decode("utf-8").strip()            
    print(response)
    print("TABLUT EINSTELLEN:")
    command =f"set game.type {GAMETYPE}\n"
    client.sendall(command.encode("utf-8"))
    response = client.recv(1024).decode("utf-8").strip()
    print(response)
    print("SCHEDULER EINSTELLEN:")       
    command =f"set scheduler {SCHEDULER}\n"
    client.sendall(command.encode("utf-8"))
    response = client.recv(1024).decode("utf-8").strip()
    print(response)

    print("MIN_PLAYERS EINSTELLEN:")       
    command =f"set min_players {MIN_PLYERS}\n"
    client.sendall(command.encode("utf-8"))
    response = client.recv(1024).decode("utf-8").strip()
    print(response)

    print("MAX_PLAYERS EINSTELLEN:")       
    command =f"set min_players {MAX_PLYERS}\n"
    client.sendall(command.encode("utf-8"))
    response = client.recv(1024).decode("utf-8").strip()
    print(response)

def registerLogin(client):
    #registrieren
    command = "register\n"
    client.sendall(command.encode("utf-8")) 
    print(f"gesendet: {command}")        
    # Antwort empfangen
    response = client.recv(1024).decode("utf-8").strip()            
    print(f"Empfangen: {response}")   
    #login
    command = f"login {response}\n"
    client.sendall(command.encode("utf-8")) 
    print(f"gesendet: {command}")  
    response = client.recv(1024).decode("utf-8").strip()            
    print(f"Empfangen: {response}")

def findLobbies(client):
    command =f"ls\n"
    client.sendall(command.encode("utf-8"))
    print(f"gesendet: {command}")  
    response = client.recv(1024).decode("utf-8").strip()            
    print(f"Empfangen: {response}") 
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
    client.sendall(command.encode("utf-8"))
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

def main():
    LOBBYCREATOR = False
    # Server-Konfiguration (Standard-Werte anpassen falls nötig)
    HOST = "127.0.0.1"  # localhost
    PORT = 5000        # Standard-Port (ggf. anpassen)

    try:
        # Verbindung zum Server herstellen
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print(f"Verbunden mit {HOST}:{PORT}")

        # Handshake-Befehl senden
        command = "gspy\n"
        client.sendall(command.encode("utf-8"))
        print(f"Gesendet: {command.strip()}")

        # Antwort empfangen
        response = client.recv(1024).decode("utf-8").strip()
        print(f"Empfangen: {response}")

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

            if LOBBYCREATOR  :
                #Creator versucht alle 3 sek Spiel zu starten, denn es kann sein das er alleine in Lobby ist, sonst spielbeginnt
                while True:
                    command = f"start\n"
                    client.sendall(command.encode("utf-8"))
                    response = client.recv(1024).decode("utf-8").strip()
                    print(response)
                    if response == "queued":                        
                        break
                    time.sleep(3)
                    
            else:
                print("Warte auf Spielstart...")
                while True:                    
                    #Es wird aus schleife rausgebrochen sobald Lobby ersteller "start drückt", Teilnehmer kriegt die Info queued.
                    response = client.recv(1024).decode("utf-8").strip()
                    if response == "queued":
                        break
                    time.sleep(20)

            print("Spielbeginnt:")   

            #TODO timeAcc,PlayerTimAccount noch anpassen
            #TODO String FEN übers Terminal anpassbar
            response = client.recv(1024).decode("utf-8").strip()
            gameType,timeAcc,playerTimeAccount,boardStr,verify = getGameData(client,response)

            print("A")
            board, onturn = debug.FenToBoard(boardStr.split("'")[1])
            print("B")
            debug.print_board(board)
            print("C")

            if gameType.split(" ")[2] != 'tablut':
                print(f"Falsches Spiel erhalten: {gameType}. Programm wird beendet.")
                sys.exit(1)

            #print(verify)
            #print(type(verify))
            if verify == 'ok':
                command = f"ok\n"
                client.sendall(command.encode("utf-8"))
                print("GESENDET! ")
            
            
            response = client.recv(1024).decode("utf-8").strip()
            if response == "start":                
                print("START")
                switchTurn(True,onturn)
                print(config.onTurn)
                myTurn(board,client)

            elif response == "wait":
                print("Wait")
                switchTurn(False,onturn)
                print(config.onTurn)
                response = client.recv(1024).decode("utf-8").strip()                
                enemyTurn(board,response)
                myTurn(board,client)
            else:
                print(f"FEHLER Response war: {response}")
            
            response = client.recv(1024).decode("utf-8").strip()
            print(response)
    
            while True:
                
                #Spielende erreicht:
                response = client.recv(1024).decode("utf-8").strip()
                if response == 'over':
                    print(f"response: {response}")
                    break
                elif response == "err 'invalid move or not your turn'":...
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