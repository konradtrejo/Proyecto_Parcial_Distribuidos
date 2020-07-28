/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package decoder.serpy;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;


/**
 *
 * @author JARED
 */
public class ServerThread extends Thread{
    Serpy s;
    
    public ServerThread(Serpy si){
        s = si;
    }
    
    @Override
    public void run(){
        try {
            s.initLoop();
        } catch (IOException ex) {
            Logger.getLogger(ServerThread.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
