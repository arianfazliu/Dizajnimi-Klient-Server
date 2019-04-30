import socket
from socket import *

host = '127.0.0.1'
port = 12000
c = socket(AF_INET, SOCK_DGRAM)
c.connect((host, port))

# per me centirat tekstin me ni lloj dekorimi:

width = 50
print("*****************MIRSEVINI*****************".center(width, '*'))

print("Universiteti i Prishtinës \"HASAN PRISHTINA.\"".center(width, '-'))
print("Fakulteti i inxhinierise elektrike dhe kompjuterike".center(width, '-'))
print("Departamenti  i kompjuterikes".center(width, '-'))
print("Lenda: Rrjeta kompjuterike".center(width, '-'))
print("UDP client".center(width, '-'))

print("\nShtypni njërën nga kërkesat e dhëna më poshtë: ")
print("===============================================")
print(
    "-IPADRESA\n-NUMRIIPORTIT\n-BASHKETINGELLORE\n-PRINTIMI\n-EMRIIKOMPJUTERIT\n-KOHA\n-LOJA\n-FIBONACCI\n-KONVERTIMI\n-RRETHI\n-FAKTORIEL\n-SCANNERSOUND")

print("Shtyp exit per te ndal lidhjen.")
print("=======================================")

while True:
    kerkesa = input("Shtypni njeren nga kerkesat: ")
    if kerkesa == "exit" or kerkesa == "EXIT":
        break
    elif (kerkesa == "PRINTIMI"):
        print("Kerkesa duhet të shkruhet keshtu: PRINTIMI fjalia ")
        continue
    elif (kerkesa == "BASHKETINGELLORE"):
        print("Kerkesa duhet të shkruhet keshtu: BASHKETINGELLORE fjala  ")
        continue
    elif (kerkesa == "FIBONACCI"):
        print("Kerkesa duhet të shkruhet keshtu: FIBONACCI numri -")
        continue
    elif (kerkesa == "KONVERTIMI"):
        print("Kerkesa duhet të shkruhet keshtu: KONVERTIMI Njesia1ToNjesia2 numri -")
        continue
    elif (kerkesa == "FAKTORIEL"):
        print("Formati i kerkeses duhet te jete: FAKTORIEL numri")
        continue
    elif (kerkesa == "ipadresa" or kerkesa == "Ipadresa"
          or kerkesa == "numriiportit" or kerkesa == "Numriiportit"
          or kerkesa == "bashketingellore" or kerkesa == "Bashketingellore"
          or kerkesa == "printimi" or kerkesa == "Printimi"
          or kerkesa == "emrikompjuterit" or kerkesa == "Emriikompjuterit" or kerkesa == "EmriIKompjuterit"
          or kerkesa == "koha" or kerkesa == "Koha"
          or kerkesa == "loja" or kerkesa == "Loja"
          or kerkesa == "fibonacci" or kerkesa == "Fibonacci"
          or kerkesa == "konverto" or kerkesa == "Konverto"
          or kerkesa == "rrethi" or kerkesa == "Rrethi"
          or kerkesa == "faktoriel" or kerkesa == "Faktoriel"
          or kerkesa == "scannersound" or kerkesa == "Scannersound"):
        print("Kerkesat duhet te shkruhen me shkronja te medha(UPPER-CASE)")
        continue



    c.send(kerkesa.encode("ASCII"))
    response = c.recv(128)
    print("Pergjigja: " + response.decode("ASCII"))
    print("***************************************")
c.close()


