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
                Storer prod = new Storer(lista, serversocket);
                prod.start();
                Serpy server = new Serpy(lista, null, serversocket);
                server.initLoop();
                break;
            case 2:
                LinkedList<char[]> lista2 = new LinkedList();
                Storer prod2 = new Storer(lista2, serversocket);
                prod2.start();
                ServerThread[] manager = new ServerThread[20];
                int i = 0;
                while(i<20){
                    Serpy server2 = new Serpy(lista2, null, serversocket);
                    manager[i] = new ServerThread(server2);
                    manager[i].start();
                    i++;
                }
                break;
            case 3:
                LinkedList<char[]>[] listan = new LinkedList[20];
                Storer[] prodn = new Storer[20];
                ServerThread[] manager2 = new ServerThread[20];
                int j = 0;
                while(j<20){
                    listan[j] = new LinkedList();
                    prodn[j] = new Storer(listan[j], serversocket);
                    prodn[j].start();
                    Serpy server2 = new Serpy(listan[j], null, serversocket);
                    manager2[j] = new ServerThread(server2);
                    manager2[j].start();
                    j++;
                }
                break;
            case 4:
                LinkedList<char[]> listaA = new LinkedList();
                LinkedList<char[]> listaB = new LinkedList();
                Storer prod4 = new Storer(listaA, serversocket);
                //Receiver recv4 = new Receiver(ListaB);
                prod4.start();
                Serpy server4 = new Serpy(listaA, listaB, serversocket);
                server4.initLoop(); 
                break;
            default:
                System.out.println(op);
        }
    }
}
