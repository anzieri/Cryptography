package com.company;

import com.company.RSA;

import java.io.*;
import java.net.*;
import java.security.*;
import java.security.spec.*;
import java.util.Base64;
import javax.crypto.*;
import javax.crypto.spec.*;

public class Alice {

    private static final int PORT = 5000; // Port for communication

    public static void main(String[] args) throws Exception {
        KeyPair keyPair = RSA.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();

        ServerSocket serverSocket = new ServerSocket(PORT);
        System.out.println("Alice (Server) is listening on port " + PORT);

        while (true) {
            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected from: " + clientSocket.getInetAddress());

            // Send public key to client
            ObjectOutputStream out = new ObjectOutputStream(clientSocket.getOutputStream());
            out.writeObject(publicKey);
            out.flush();

            // Receive encrypted message from client
            ObjectInputStream in = new ObjectInputStream(clientSocket.getInputStream());
            String encryptedMessage = (String) in.readObject();

            //visualize
            System.out.println("Encrypted message: "+ encryptedMessage);

            // Decrypt message and print
            String decryptedMessage = RSA.decrypt(encryptedMessage, keyPair.getPrivate());
            System.out.println("Received message from Bob: " + decryptedMessage);

            // Close connection for this client
            clientSocket.close();
        }
    }
}
