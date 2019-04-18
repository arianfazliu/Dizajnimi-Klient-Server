from socket import *
from random import randint
import re
import string
import datetime
import math
from math import pow
import winsound

port = 12000
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', port))


# =========METODAT============

def IPADRESA():
    PRINT = "IP adresa e klientit eshte: " + address[0]
    s.sendto(str(PRINT).encode("ASCII"), address)


def NUMRIIPORTIT():
    PRINT = "Klienti eshte duke perdorur portin: " + str(address[1])
    s.sendto(PRINT.encode("ASCII"), address)


def PRINTIMI(kerkesa):
    splitKerkesa = kerkesa.split(" ")
    i = 1
    stringtext = ""

    while i<len(splitKerkesa):
        stringtext = stringtext + splitKerkesa[i] + " "
        i += 1
        PRINT = stringtext
    s.sendto(PRINT.encode("ASCII"), address)


def BASHKETINGELLORE(x):
    bashketingellore = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C',
                        'D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    numeratori=0
    for shkronja in x:
        if(shkronja in bashketingellore):
            numeratori = numeratori+1
            rezultati = "Teksti i pranuar permban " + str(numeratori-10) + " bashketingellore"
    return rezultati
    PRINT = rezultati
    s.sendto(PRINT.encode("ASCII"), address)


def PCNAME():
    try:
        emriipc = gethostbyaddr(address[0])
        response = "Emri i klientit eshte " + str(emriipc[0])
    except ValueError:
        response = "Emri i klientit nuk dihet."
    s.sendto(response.encode("ASCII"), address)


def KOHA():
    now = datetime.datetime.now()
    PRINT = now.strftime('%d.%m.%Y %H:%M:%S %p')
    s.sendto(PRINT.encode("ASCII"), address)


def LOJA():
    Numrat = []
    for i in range(0, 7):
        Numrat.append(randint(1, 49))
    PRINT = str(Numrat)
    s.sendto(PRINT.encode("ASCII"), address)



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
    PRINT = str(round(output, 2))
    s.sendto(PRINT.encode("ASCII"), address)

def FIBONACCI(numri):
    if numri == 0:
        return 0
    elif numri == 1:
        return 1
    else:
        rezultati = FIBONACCI(numri-1)+FIBONACCI(numri-2)

    return rezultati


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
                + str("%.2f" % P_rrethit) + ", S=" + str("%.2f" % S_rrethit)
        s.sendto(PRINT.encode("ASCII"), address)

def SCANNERSOUND():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 400  # Set Duration To 1000 ms == 1 second
    for PRINT in range(0, 5):
        PRINT = "Tani do te degjohet zeri: " +str(winsound.Beep(frequency, duration))
        s.sendto(PRINT.encode("ASCII"), address)



while True:
    print("--------------Duke pritur per kerkesa te klienteve--------------")
    kerkesa, address = s.recvfrom(1024)

    point = kerkesa.decode("ASCII")
    points = point.split(' ')
    message = points[0]

    print("Kerkesa e pranuar eshte: " + point)
    if message == "IPADRESA":
        IPADRESA()
    elif message == "NUMRIIPORTIT":
        NUMRIIPORTIT()
    elif message == "EMRIIKOMPJUTERIT":
        PCNAME()
    elif message == "KOHA":
        KOHA()
    elif message == "LOJA":
        LOJA()
    elif message == "KONVERTIMI":
        if points[2].isdigit():
            konverto = points[1]
            vlera = points[2]
            KONVERTIMI(konverto, vlera)
        else:
            PRINT = "Formati i kerkeses duhet te jete: KONVERTO NjesiaPareToNjesiaDyte numri -"
            s.sendto(PRINT.encode("ASCII"), address)
    elif message == "PRINTIMI":
        PRINTIMI(point)

    elif message == "BASHKETINGELLORE":
        rezultati = str(BASHKETINGELLORE(point))
        s.sendto(rezultati.encode("ASCII"), address)
    elif message == "SCANNERSOUND":
        SCANNERSOUND()
    elif message == "FIBONACCI":
        rezultati = str(FIBONACCI(int(points[1])))
        s.sendto(rezultati.encode("ASCII"), address)

    elif message == "RRETHI":
        if points[1].isdigit():
            RRETHI(points[1])
        else:
            PRINT = "Formati i kerkeses duhet te jete RRETHI rrezja -"
            s.sendto(PRINT.encode("ASCII"), address)
    elif message == "FAKTORIEL":

                result = str(FAKTORIEL(int(points[1])))
                s.sendto(result.encode("ASCII"), address)


    else:
        PRINT = "Ka ndodhur nje gabim gjate shkruarjes se kerkeses!"
        s.sendto(PRINT.encode("ASCII"), address)

