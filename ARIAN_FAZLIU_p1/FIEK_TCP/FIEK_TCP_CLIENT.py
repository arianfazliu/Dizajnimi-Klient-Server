from socket import *

IP = "localhost"
PORT = int(input("Shkruani portin në të cilin dëshironi të lidheni: "))
print("\n")

s = socket(AF_INET, SOCK_STREAM)
s.connect((IP, PORT))

width = 50
print("*****************MIRSEVINI*****************".center(width, '*'))

print("Universiteti i Prishtinës \"HASAN PRISHTINA.\"".center(width, '-'))
print("Fakulteti i inxhinierise elektrike dhe kompjuterike".center(width, '-'))
print("Departamenti  i kompjuterikes".center(width, '-'))
print("Lenda: Rrjeta kompjuterike".center(width, '-'))
print("TCP client".center(width, '-'))

print("\nShtypni njërën nga kërkesat e dhëna më poshtë: ")
print("===============================================")
print("-IPADRESA\n-NUMRIIPORTIT\n-BASHKETINGELLORE\n-PRINTIMI\n-EMRIIKOMPJUTERIT\n-KOHA\n-LOJA\n-FIBONACCI\n-KONVERTIMI\n-RRETHI\n-FAKTORIEL\n-SCANNERSOUND")

print("Shtyp exit per te ndal lidhjen.")
print("=======================================")

while True:
    kerkesa = input("Shtypni njeren nga kerkesat: ")
    if kerkesa == "exit" or kerkesa == "EXIT":
        break
    elif(kerkesa == "PRINTIMI"):
        print("Kerkesa duhet të shkruhet keshtu: PRINTIMI fjalia ")
        continue
    elif(kerkesa == "BASHKETINGELLORE"):
        print("Kerkesa duhet të shkruhet keshtu: BASHKETINGELLORE fjala  ")
        continue
    elif(kerkesa == "FIBONACCI"):
        print("Kerkesa duhet të shkruhet keshtu: FIBONACCI numri -")
        continue
    elif(kerkesa == "KONVERTIMI"):
        print("Kerkesa duhet të shkruhet keshtu: KONVERTIMI Njesia1ToNjesia2 numri -")
        continue
    elif(kerkesa == "FAKTORIEL"):
        print("Formati i kerkeses duhet te jete: FAKTORIEL numri")
        continue
    elif (kerkesa == "RRETHI"):
        print("Formati i kerkeses duhet te jete: RRETHI rrezja")
        continue
    elif(kerkesa == "ipadresa" or kerkesa == "Ipadresa"
         or kerkesa == "numriiportit" or kerkesa == "Numriiportit"
         or kerkesa == "bashketingellore" or kerkesa == "Bashketingellore"
         or kerkesa == "printimi" or kerkesa == "Printimi"
         or kerkesa == "emrikompjuterit" or kerkesa == "Emriikompjuterit" or kerkesa == "EmriIKompjuterit"
         or kerkesa == "koha" or kerkesa == "Koha"
         or kerkesa == "loja" or kerkesa == "Loja"
         or kerkesa == "fibonacci" or kerkesa == "Fibonacci"
         or kerkesa == "konvertimi" or kerkesa == "Konvertimi"
         or kerkesa == "rrethi" or kerkesa == "Rrethi"
         or kerkesa == "faktoriel" or kerkesa == "Faktoriel"
         or kerkesa == "scannersound" or kerkesa == "Scannersound"):

        print("Kerkesat duhet te shkruhen me shkronja te medha(UPPER-CASE)")
        continue
    s.send(kerkesa.encode("ASCII"))
    response = s.recv(128)
    print("Pergjigja: " + response.decode("ASCII"))
    print("***************************************")

s.close()

