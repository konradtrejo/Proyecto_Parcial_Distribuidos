/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package decoder.serpy;

import java.io.IOException;
import java.net.ServerSocket;
import java.util.LinkedList;

/**
 *
 * @author JARED
 */
public class Main {
    public static void main(String[] args) throws IOException{
        int port = 2018;
        
        ServerSocket serversocket = new ServerSocket(port);
        
        System.out.println("Ingrese opcion:");
        System.out.println("1: Cliente unico");
        System.out.println("2: Cola unica para todos");
        System.out.println("3: Cola nueva por cada cliente");
        System.out.println("4: Cola reactiva");
        int op = System.in.read()-48;
        switch(op){
            case 1:
                LinkedList<char[]> lista = new LinkedList();
                Producer prod = new Producer(lista);
                prod.start();
                Serpy server = new Serpy(lista, null, serversocket, prod);
                server.initLoop();
                break;
            case 2:
                LinkedList<char[]> lista2 = new LinkedList();
                Producer prod2 = new Producer(lista2);
                prod2.start();
                ServerThread[] manager = new ServerThread[20];
                int i = 0;
                while(i<20){
                    Serpy server2 = new Serpy(lista2, null, serversocket, prod2);
                    manager[i] = new ServerThread(server2);
                    manager[i].start();
                    i++;
                }
                break;
            case 3:
                LinkedList<char[]>[] listan = new LinkedList[20];
                Producer[] prodn = new Producer[20];
                ServerThread[] manager2 = new ServerThread[20];
                int j = 0;
                while(j<20){
                    listan[j] = new LinkedList();
                    prodn[j] = new Producer(listan[j]);
                    prodn[j].start();
                    Serpy server2 = new Serpy(listan[j], null, serversocket, prodn[j]);
                    manager2[j] = new ServerThread(server2);
                    manager2[j].start();
                    j++;
                }
                break;
            case 4:
                LinkedList<char[]> listaA = new LinkedList();
                LinkedList<char[]> listaB = new LinkedList();
                Producer prod4 = new Producer(listaA);
                //Receiver recv4 = new Receiver(ListaB);
                prod4.start();
                Serpy server4 = new Serpy(listaA, listaB, serversocket, prod4);
                server4.initLoop(); 
                break;
            default:
                System.out.println(op);
        }
    }
}
