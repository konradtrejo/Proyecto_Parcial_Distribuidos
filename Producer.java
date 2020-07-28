/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package decoder.serpy;

import java.net.InetAddress;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author JARED
 */
public class Producer {
    public static void main(String[] args){
        int n = 0;
        MiddleLibJa.init("192.168.1.3");
        while(true){
            //System.out.println("Yendo...");
            try{
                Thread.sleep(2000);
            }catch (InterruptedException ex) {
                Logger.getLogger(Producer.class.getName()).log(Level.SEVERE, null, ex);
            }
            MiddleLibJa.send("Producto " + n);
            n++;
        }
        //MiddleLibJa.close();
    }
}
