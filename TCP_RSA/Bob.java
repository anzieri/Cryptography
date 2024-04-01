package com.company;

import com.company.RSA;

import java.io.*;
import java.net.*;
import java.security.*;
import java.security.spec.*;
import java.util.Base64;
import javax.crypto.*;
import javax.crypto.spec.*;

public class Bob {

    private static final String HOST = "localhost"; // Alice's server address
    private static final int PORT = 5000; // Port for communication

    public static void main(String[] args) throws Exception {
        KeyPair keyPair = RSA.generateKeyPair();

        // Connect to server
        Socket clientSocket = new Socket(HOST, PORT);
        System.out.println("Bob (Client) connected to Alice (Server): " + clientSocket.getRemoteSocketAddress());

        // Receive public key from server
        ObjectInputStream in = new ObjectInputStream(clientSocket.getInputStream());
        PublicKey publicKey = (PublicKey) in.readObject();
        System.out.println(publicKey);
        // Get message to send

        String message = "Hello from Bob!";

        // Encrypt message using server's public key
        String encryptedMessage = RSA.encrypt(message, publicKey);

        // Send encrypted message to server
        ObjectOutputStream out = new ObjectOutputStream(clientSocket.getOutputStream());
        out.writeObject(encryptedMessage);
        out.flush();

        // Close connection
        clientSocket.close();
    }
}
