/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package decoder.serpy;
import java.io.*;
import java.net.*;
import java.util.LinkedList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author JARED
 */
public class Serpy {

    LinkedList<char[]> send;
    LinkedList<char[]> recv;
    Producer prod;
    ServerSocket server;
    Socket cli;

    public Serpy(LinkedList<char[]> li, LinkedList<char[]> ki, ServerSocket s, Producer prodi) throws IOException {
        send = li;
        recv = ki;
        prod = prodi;
        server = s;
        System.out.println("Esperando cliente");
        cli = server.accept();
    }
    
    public void initLoop() throws IOException {
        //String recibido = "", enviado = "";
        OutputStreamWriter outw = new OutputStreamWriter(cli.getOutputStream(), "UTF8");
        InputStreamReader inw = new InputStreamReader(cli.getInputStream(), "UTF8");
        System.out.println("Cliente conseguido!");
        
        if(recv!=null){
            Receiver rcv = new Receiver(recv, inw);
            rcv.start();
        }
        while(true){
            // Si no refresca, por alguna razón no produce...
            try{
                Thread.sleep(250);
            }catch (InterruptedException ex) {
                Logger.getLogger(Producer.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            if(send.peekFirst()!=null){
                char[] p = send.removeFirst();
                outw.write(p);
                outw.flush();
            }
            
            //System.out.println("Esperando mensaje del cliente en python");
            /*
            inw.read(cbuf);
            for (char c : cbuf) {
                recibido += c;
                if (c == 00) {
                    break;
                }
            }
            */
            //System.out.println("Cliente dice: " + recibido);
            //System.out.println("Enviar a cliente: >>>" + recibido);
            //recibido = "S:" + recibido;
            //outw.write(recibido.toCharArray());
            //outw.flush();
            //cbuf = new char[512];
            //recibido = "";
        }

    }
}