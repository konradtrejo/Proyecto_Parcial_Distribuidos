/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package decoder.serpy;

import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;
import java.util.LinkedList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author JARED
 */
public class Storer extends Thread{
    LinkedList l;
    boolean running;
    InputStreamReader inw;
    
    public Storer(LinkedList li, ServerSocket s) throws IOException{
        l = li;
        running = true;
        System.out.println("Esperando cliente");
        Socket cli = s.accept();
        inw = new InputStreamReader(cli.getInputStream(), "UTF8");
    }
    
    @Override
    public void run(){
        int n = 0;
        while(running){
            try {
                String recibido = "";
                char[] cbuf = new char[512];
                inw.read(cbuf);
                
                for (char c : cbuf) {
                    recibido += c;
                    if (c == 00) {
                        break;
                    }
                }
                l.addLast(recibido.toCharArray());
            } catch (IOException ex) {
                Logger.getLogger(Receiver.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
}
