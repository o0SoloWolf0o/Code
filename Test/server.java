package Test;

import java.io.*;
import java.net.*;

public class server {
    public static void main(String[] args){
        try{
            ServerSocket ss = new ServerSocket(6789);
            System.out.println("A socket is created and now waiting for connection.");
            Socket s = ss.accept();
            System.out.println("A client has made a connection in.");
            DataInputStream din = new DataInputStream(s.getInputStream());
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            System.out.println("Waiting for an incoming message...");
            String str = (String)din.readUTF();
            System.out.println("Message received: " + str);
            str = str + " " + str;
            System.out.println("Now I'm going to write this message backL" + str);
            dout.writeUTF(str);
            ss.close();
        }catch(Exception e){System.out.println(e);}
    }
}

