/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package decoder.serpy;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author JARED
 */
public class MiddleLibJa {
    static Socket dir;
    static OutputStreamWriter outw;
    
    public static void init(String ip){
        outw = null;
        try {
            dir = new Socket(InetAddress.getByName(ip), 2018);
            outw = new OutputStreamWriter(dir.getOutputStream(), "UTF8");
        } catch (IOException ex) {
            Logger.getLogger(MiddleLibJa.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    public static void send(String s){
        try {
            outw.write(s);
            outw.flush();
        } catch (IOException ex) {
            Logger.getLogger(MiddleLibJa.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    public static void close(){
        try {
            outw.close();
            dir.close();
        } catch (IOException ex) {
            Logger.getLogger(MiddleLibJa.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
