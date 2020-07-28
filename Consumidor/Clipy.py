import sys
import socket as sk

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

    def consumir(self):
        ins = self.sCliente.recv(512)
        insd = ins.decode("UTF8")
        return (str(insd))

    def producir(self,texto):
        self.sCliente.send(texto)
        print("Enviando "+texto)
        
        """
        while seguir:
            ints = "1"
            ins = self.sCliente.send(ints)
            #insd = ins.decode("UTF8")
            print("Cliente produciendo: " + str(ints))
        """

"""
host = "127.0.0.1"
port = 2018  

cliente1 = conexion_cliente(host, port)
cliente1.conectar()
seguir = True
while(seguir):
    consumo = cliente1.consumir()
    print(consumo)
cliente1.desconectar()
print("Terminado")

"""