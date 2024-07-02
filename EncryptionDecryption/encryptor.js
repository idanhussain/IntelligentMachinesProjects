/**
 * Authors: Idan Hussain, Edaad Azman
 * Encryptor Function
 */

import JSEncrypt from 'jsencrypt';
// npm install jsencrypt

function encryptData(password, publicKey) {
    const encrypt = new JSEncrypt();
            encrypt.setPublicKey(publicKey);
            const encrypted = encrypt.encrypt(password);
            return encrypted;
}