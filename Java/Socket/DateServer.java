import java.net.*;
import java.io.*;

public class DateServer {
    public static void main(String[] args) {
        try {
            ServerSocket sock = new ServerSocket(6013);

            // listen for connections
            while (true) {
                Socket client = sock.accept();
                
                PrintWriter pout = new PrintWriter(client.getOutputStream(), true);

                // Write Date to socket
                pout.println(new java.util.Date().toString());

                // Close socket and resume listening
                client.close();
            }

        } catch (IOException ioe) {
            System.err.println(ioe);
        }
    }
}