import socket
from socket import gethostbyaddr
# from socket import gethostbyname
import string
import datetime
from threading import Thread
from socketserver import ThreadingMixIn
import math
from math import pow
import random
from random import randint
import winsound




#=========METODAT============
def IPADRESA():
    hostname = socket.gethostname()
    ipadress = socket.gethostbyname(hostname)
    gjatesia = len(ipadress)
    if (gjatesia <= 128):
        PRINT = "IP Adresa e klientit eshte: " + str(ipadress)
    else:
        PRINT = "Mesazhi permban me shume se 128 karaktere"
    conn.send(PRINT.encode("ASCII"))


def NUMRIIPORTIT():
    PRINT = "Klienti eshte duke perdorur portin: " + str(port)
    conn.send(PRINT.encode("ASCII"))



def BASHKETINGELLORE(x):
    bashketingellore = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C',
                        'D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    numeratori=0
    gjatesiaetekstit = len(x)
    if(gjatesiaetekstit <= 128):
        for shkronja in x:
            if(shkronja in bashketingellore):
                numeratori = numeratori+1
                rezultati = "Teksti i pranuar permban " + str(numeratori-10) + " bashketingellore"
            else:
                rezultati = "Mesazhi duhet te jete < 128"
        return rezultati





def PRINTIMI(kerkesa):
    splitKerkesa = kerkesa.split(" ")
    i = 1
    stringtext = ""

    while i<len(splitKerkesa):
        stringtext = stringtext + splitKerkesa[i] + " "
        i += 1
        PRINT = stringtext
        conn.send(PRINT.encode("ASCII"))



def PCNAME():
    try:
        emriipc = gethostbyaddr(ip)
        response = "Emri i klientit eshte " + str(emriipc[0])
    except ValueError:
        response = "Emri i klientit nuk dihet."
    PRINT = response
    conn.send(PRINT.encode("ASCII"))

def KOHA():
    now = datetime.datetime.now()
    PRINT = now.strftime('%d.%m.%Y %H:%M:%S %p')
    conn.send(PRINT.encode("ASCII"))



def LOJA():
    Numrat = []
    for i in range(0, 7):
        Numrat.append(randint(1, 49))
    PRINT = str(Numrat)
    conn.send(PRINT.encode("ASCII"))


def FIBONACCI(numri):
    if numri == 0:
        return 0
    elif numri == 1:
        return 1
    else:
        rezultati = FIBONACCI(numri-1)+FIBONACCI(numri-2)

        return rezultati


def KONVERTIMI(konverto,numer):
    input = float(numer)
    output = 0
    if(konverto == "KilowattToHorsepower"):
        output = input * 1.341
    elif(konverto == "HorsepowerToKilowatt"):
        output = input / 1.341
    elif(konverto == "DegreesToRadians"):
        output = input * 3.14/180
    elif(konverto == "RadiansToDegrees"):
        output = input * 180/3.14
    elif(konverto == "GallonsToLiters"):
        output = input * 3.785
    elif(konverto == "LitersToGallons"):
        output = input / 3.785
    PRINT = str(output)
    conn.send(PRINT.encode("ASCII"))




# ===========Metodat shtese===============

def FAKTORIEL(num):

    faktoriel = 1
    # nje loop me tregu se a eshte numri negativ. pozitiv apo zero
    if num < 0:
        print("Numri faktoriel nuk ekziston per numra negativ!")
    elif num == 0:
        print("Numri faktoriel i zero-s eshte 1")
    else:
        for i in range(1, num + 1):
            faktoriel = faktoriel * i
        result = faktoriel
        return result

def RRETHI(rrezja):

        rrezja=float(rrezja)
        P_rrethit = 2*math.pi * rrezja
        S_rrethit = math.pi * math.pow(rrezja, 2)
        round(P_rrethit, 2)
        PRINT = "\nPerimetri dhe Syprina e rrethit me rreze " + str("%.0f" % rrezja) + " jane P=" \
                + str("%.2f" % P_rrethit) + ", S=" + str("%.2f" %S_rrethit)
        conn.send(PRINT.encode("ASCII"))

def SCANNERSOUND():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 400  # Set Duration To 1000 ms == 1 second
    for PRINT in range(0, 5):
        PRINT = "Tani do te degjohet zeri: " +str(winsound.Beep(frequency, duration))
        conn.send(PRINT.encode("ASCII"))


class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("Nje klient i ri eshte lidhur me IP: --> " + ip + "ne PORT: " + str(port))

    def run(self):
        while True:
            try:
                data = conn.recv(1024)
            except socket.error:
                print("--------------Duke pritur per kerkesa te klienteve--------------")
                break
            point = data.decode("ASCII")
            points = point.split(' ')
            message = points[0]
            print("Kerkesa e pranuar nga porti - "+str(port) + " : " + point)
            if message == 'exit':
                break
            elif message == "IPADRESA":
                IPADRESA()
            elif message == "NUMRIIPORTIT":
                NUMRIIPORTIT()

            elif message == "BASHKETINGELLORE":
                 rezultati = str(BASHKETINGELLORE(point))
                 conn.send(rezultati.encode("ASCII"))

            elif message == "PRINTIMI":
                 PRINTIMI(point)

            elif message == "EMRIIKOMPJUTERIT":
                 PCNAME()

            elif message == "KOHA":
                 KOHA()

            elif message == "LOJA":
                 LOJA()

            elif message == "FIBONACCI":
                rezultati = str(FIBONACCI(int(points[1])))
                conn.send(rezultati.encode("ASCII"))

            elif message == "KONVERTIMI":
                if points[2].isdigit():
                    konverto = points[1]
                    vlera = points[2]
                    KONVERTIMI(konverto, vlera)
                else:
                    PRINT = "Formati i kerkeses duhet te jete: KONVERTO NjesiaPareToNjesiaDyte numri -"
                    conn.send(PRINT.encode("ASCII"))

            elif message == "RRETHI":
                if points[1].isdigit():
                    RRETHI(points[1])
                else:
                    PRINT = "Formati i kerkeses duhet te jete RRETHI rrezja -"
                    conn.send(PRINT.encode("ASCII"))

            elif message == "FAKTORIEL":

                result = str(FAKTORIEL(int(points[1])))
                conn.send(result.encode("ASCII"))

            elif message == "SCANNERSOUND":
                SCANNERSOUND()


            else:
                PRINT = "Ka ndodhur nje gabim gjate shkruarjes se kerkeses!"
                conn.send(PRINT.encode("ASCII"))

TCP_IP = '127.0.0.1'
TCP_PORT = 12000
BUFFER_SIZE = 1024

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []
print("--------------Serveri eshte gatshem per te pranuar kerkese--------------")
while True:
    tcpServer.listen(5)
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()