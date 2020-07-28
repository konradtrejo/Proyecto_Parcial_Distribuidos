/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package decoder.serpy;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author JARED
 */
public class Receiver extends Thread{
    LinkedList l;
    boolean running;
    InputStreamReader inw;
    
    public Receiver(LinkedList<char[]> li, InputStreamReader in){
        l = li;
        inw = in;
        running = true;
    }
    
    @Override
    public void run(){
        // Buffer para lectura
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
                System.out.println(recibido);
            } catch (IOException ex) {
                Logger.getLogger(Receiver.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
}
