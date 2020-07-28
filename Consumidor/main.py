from ventana import *
from Clipy import *
import time

#rc4,escitala,cifrado_cesar,cifrado_veginere,cifrado_xor

class MainWindows(QtWidgets.QMainWindow,Ui_conexion):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)

        self.host = "127.0.0.1"
        self.port = 2018  

        self.Thost.setText(self.host)
        self.Tport.setText(str(self.port))
        
        self.seguir = True
        
        self.Cliente = conexion_cliente(self.host, self.port)
        
        self.Bconectar.clicked.connect(self.conectar)
        self.Bdesconectar.clicked.connect(self.desconectar)
        self.Bconsumir.clicked.connect(self.consumir)
        self.Bproducir.clicked.connect(self.actualizar)
        
    def conectar(self):
        self.host = self.Thost.toPlainText()
        self.port = int(self.Tport.toPlainText())
        self.Cliente.set_host_port(self.host,self.port)
        self.Tlogs.append("Conectandose a "+(self.host)+":"+str(self.port))
        self.Cliente.conectar()
        self.Tlogs.append("Conectado")
        
    def desconectar(self):
        self.seguir = False
        self.Tlogs.append("Desconectando...")
        self.Cliente.desconectar()
        self.Tlogs.append("Desconectado")
        
    def consumir(self):
        self.Tlogs.append("Consumiendo...")
        #cont = 0
        #while(self.seguir):
        for i in range(10):
            consumo = self.Cliente.consumir()
            self.Tlogs.append(consumo)
            #time.sleep(1)
            """cont +=1
            if(cont>10):
                self.actualizar()
            """
            
    def actualizar(self):
        self.seguir = False



if __name__=="__main__":
    
    app = QtWidgets.QApplication([])
    windows = MainWindows()
    windows.move(250,0)
    windows.show()
    app.exec_()

