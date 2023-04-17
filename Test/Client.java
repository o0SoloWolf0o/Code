package Test;

import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args){
        try{
            Socket s = new Socket("localhost", 6789);
            System.out.println("A connection is established and I'll now.");
            DataInputStream din = new DataInputStream(s.getInputStream());
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            dout.writeUTF("Hello Server");
            dout.flush();
            String str = (String)din.readUTF();
            System.out.println("Message received from server: " + str);
            dout.close();
            s.close();
        }catch(Exception e){
            System.out.println(e);
        }
    }
}
