package com.company;

import javax.crypto.Cipher;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.*;
import java.util.Arrays;
import java.util.Base64;

public class RSA {

    private static final int KEY_SIZE = 1024;

    public static KeyPair generateKeyPair() throws NoSuchAlgorithmException, InvalidAlgorithmParameterException {
        KeyPairGenerator generator = KeyPairGenerator.getInstance("RSA");
        generator.initialize(KEY_SIZE);
        return generator.generateKeyPair();
    }

    public static String encrypt(String message, PublicKey publicKey) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPWithSHA1AndMGF1Padding");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        byte[] messageBytes = message.getBytes(StandardCharsets.UTF_8);
        byte[] encryptedBytes = cipher.doFinal(messageBytes);
        return Base64.getEncoder().encodeToString(encryptedBytes);
    }

    public static String decrypt(String encryptedMessage, PrivateKey privateKey) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPWithSHA1AndMGF1Padding");
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] encryptedBytes = Base64.getDecoder().decode(encryptedMessage);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
        return new String(decryptedBytes, StandardCharsets.UTF_8);
    }

//    public static boolean isPrime(int num){
//        if(num==1) return false;
//        int[] prime = {2,3,5,7,9,11,13,17,19, 23, 29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101};
//        for(int i= 0; i< prime.length;i++ )
//            if(num%prime[i]!=0 || num==prime[i]){
//                //System.out.println("Possible");
//            }else{
//                //System.out.println("Divisble");
//                return false;
//            }
//        return true;
//    }
//
//    public static BigInteger bytesToBigInteger(byte[] bytes) {
//        System.out.println(new BigInteger(bytes));
//        return new BigInteger(bytes);
//    }
//
//    public static byte[] bigIntegerToBytes(BigInteger bigInteger) {
//        System.out.println(Arrays.toString(bigInteger.toByteArray()));
//        return bigInteger.toByteArray();
//    }
//
//    public static byte[] stringToBytes(String str) {
//        System.out.println(Arrays.toString(str.getBytes(StandardCharsets.UTF_8)));
//        return str.getBytes(StandardCharsets.UTF_8);
//    }
//
//    public static String bytesToString(byte[] bytes) {
//        System.out.println(new String(bytes, StandardCharsets.UTF_8));
//        return new String(bytes, StandardCharsets.UTF_8);
//    }
//
//    public static int calculateGCD(int a, int b) {
//        while (b != 0) {
//            int temp = b;
//            b = a % b;
//            a = temp;
//        }
//        return a;
//    }
//
//    public static int getRange(int max, int min){
//        int num = (int) (Math.random() * (max - min+ 1)+min);
//        System.out.println(num);
//        return num;
//    }
//
//    public static int[] generateKeyPair(){
//        int[] key = new int[2];
//        int p = Other.getRange(20, 6);
//        int q = Other.getRange(67, 40);
//
//        while (!(Other.isPrime(p) && Other.isPrime(q))) {
//            p = Other.getRange(20, 6);
//            q = Other.getRange(67, 40);
//        }
//        int n = p*q;
//        int phi = (p-1)*(q-1);
//        int e = getRange(phi, 2);
//        int GCD = calculateGCD(phi, e);
//        while(GCD != 1){
//            e = getRange(phi, 2);
//            GCD = calculateGCD(phi, e);
//        }
//        key[0] = e;
//        key[1] = n;
//        return key;
//    }
//    public static BigInteger RSAEncrypt(int[] keys, int message) {
//        BigInteger cipher;
//        int e = keys[0];
//        int n = keys[1];
//        int[] prime = {2,3,5,7,9,11,13,17,19, 23, 29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101};
//        int p = 0;
//        int q = 4;
//        int i = -1;
//        while(!isPrime(q)){
//            i++;
//            if(n%prime[i]==0) {
//                q = prime[i];
//            }
//        }
//        p = (n/q);
//        int phi = (p-1)* (q-1);
//        //c = m^e mod n
//
//        BigInteger Mine = new BigInteger(String.valueOf(message));
//        BigInteger result = Mine.pow(e);
//
//        cipher = result.mod(BigInteger.valueOf(n));
//
//        System.out.println("Our n (qxp) = " + n);
//        System.out.println("Euler's totient is: " + phi);
//        System.out.println("Our e is: " + e);
//        System.out.println("Result: "+ result);
//        System.out.println("p and q: "+ p + " " + q);
//        System.out.println("Your new cipher is: " + cipher);
//        int[] publickey = {e, n};
//
//        return cipher;
//    }
//
//    public static BigInteger RSADecrypt(int cipher, int[] key ) {
//        BigInteger message= new BigInteger("0");
//        int[] prime = {2,3,5,7,9,11,13,17,19, 23, 29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101};
//        int p = 0;
//        int q = 4;
//        int i = -1;
//        int e = key[0];
//        int n = key[1];
//        while(!isPrime(q)){
//            i++;
//            if(n%prime[i]==0) {
//                q = prime[i];
//            }
//        }
//
//        p = (n/q);
//        int phi = (p-1)* (q-1);
//        BigDecimal d= new BigDecimal(String.valueOf(((1/e)) ));
//        BigInteger ex = new BigInteger(String.valueOf(e));
//        BigInteger answer = ex.modInverse(BigInteger.valueOf(phi));
//        BigInteger c = new BigInteger(String.valueOf(cipher));
//        BigInteger mine = c.pow(answer.intValue());
//        BigInteger result = mine.mod(BigInteger.valueOf(n));
//
//
//        System.out.println("The totient(phi): "+ phi);
//        System.out.println("D: "+ answer);
//        System.out.println("mine: "+ mine);
//        System.out.println("Message: "+ result);
//        return result;
//    }
}
