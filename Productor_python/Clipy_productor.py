import sys
import socket as sk
import time

class conexion_cliente:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sCliente = sk.socket()

    def set_host_port(self,host,port):
        self.host = host
        self.port = port
        
    def conectar(self):
        print("Iniciando conexión")
        self.sCliente.connect((self.host, self.port))
        print("Conectado")

    def desconectar(self):
        #print("Desconectando...")
        self.sCliente.close()
        print ("Desconectado")

    def producir(self,texto):
        self.sCliente.send(texto)
        print("Enviando "+texto)
        

"""
host = "127.0.0.1"
port = 2018  

cliente1 = conexion_cliente(host, port)
cliente1.conectar()
seguir = True
cont = 0
while(seguir):
    consumo = cliente1.producir("Producto "+str(cont))
    print(consumo)
    time.sleep(2)
cliente1.desconectar()
print("Terminado")

"""