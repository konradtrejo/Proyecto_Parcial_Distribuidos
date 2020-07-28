import sys
import time
import threading
import socket as sk

def Productor():
    i = 0
    while(True):
        time.sleep(2)
        inp = "Producto " + str(i)
        salida = inp.encode("UTF8")
        i = i + 1
        sCliente.send(salida)
        salida = None
    return

host = "127.0.0.1"
port = 2018

sCliente =  sk.socket()
sCliente.connect((host, port))
print("Conectado")
inp = input("Definir modo:\n1:Cliente receptor\n2:Cliente reactivo\n")
#out = inp.encode("UTF8")
#print("Se ha enviado: " + str(out.decode("UTF-8")))
#sCliente.send(out)
seguir = True
if inp == "2":
    t = threading.Thread(target = Productor)
    t.start()
while seguir:
    ins = sCliente.recv(512)
    insd = ins.decode("UTF8")
    print("Servidor retorna: " + str(insd))
    #inp = input("Texto para enviar:")
    #print("Enviar " + str(inp))
    #salida = inp.encode("UTF8")
    #print("Salida tiene antes de enviar: " + str(salida.decode("utf8")))
    #lene = sCliente.send(salida)
    #print("Se han enviado: " + str(lene) + " :bytes al servidor")
    #if inp == "exit":
        #seguir = False
    #salida = None
    #ins = ""
sCliente.close()
print("Terminado")

