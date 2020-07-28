from ventana import *
from Clipy_consumidor import *
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
        
        self.producto_cont = 0
        
        self.seguir = True
        
        self.Cliente = conexion_cliente(self.host, self.port)
        
        self.Bconectar.clicked.connect(self.conectar)
        self.Bdesconectar.clicked.connect(self.desconectar)
        self.Bconsumir.clicked.connect(self.consumir)
        self.Bproducir.clicked.connect(self.producir)
        self.Bproducir.setVisible(False)
        
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
            self.Tlogs.append("Servidor retorna: " + consumo)
            respuesta = self.procesar_factorial(consumo)
            if(respuesta != 0):
                self.Tlogs.append("Factorial de "+consumo[6:]+": " + str(respuesta))
            
    def procesar_factorial(self,texto):
        if("facto " in texto):
            numero = texto[6:]
            if(numero.isnumeric()):
                return self.factorial(int(numero))
            else:
                return 0
        else:
            return 0
        
    def factorial(self,numero):
        if(numero == 0):
            return 1
        arr = list(range(numero+1))[1:]
        final = 1
        for i in arr:
            final *= i
        return final
        
    def actualizar(self):
        self.seguir = False
        
    def producir(self):
        for i in range(10):
            texto = "Producto "+self.producto_cont
            self.Cliente.producir(texto)
            self.Tlogs.append("Enviando : " + texto)
            self.producto_cont += 1
            time.sleep(2)
        



if __name__=="__main__":
    
    app = QtWidgets.QApplication([])
    windows = MainWindows()
    windows.move(250,0)
    windows.show()
    app.exec_()

