/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package decoder.serpy;

import java.util.LinkedList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author JARED
 */
public class Producer extends Thread{
    LinkedList l;
    boolean running;
    
    public Producer(LinkedList li){
        l = li;
        running = true;
    }
    
    @Override
    public void run(){
        int n = 0;
        while(running){
            //System.out.println("Yendo...");
            try{
                Thread.sleep(2000);
            }catch (InterruptedException ex) {
                Logger.getLogger(Producer.class.getName()).log(Level.SEVERE, null, ex);
            }
            l.addLast(("Producto " + n).toCharArray());
            n++;
        }
    }
}
