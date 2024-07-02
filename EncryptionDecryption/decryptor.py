# Authors: Idan Hussain, Edaad Azman
# Encryptor Function

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
# pip install cryptography

def decrypt_data(encrypted_text, private_key):
    private_key = serialization.load_pem_private_key(
        private_key.encode(),
        password=None,
    )
    decrypted = private_key.decrypt(
        encrypted_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=SHA256()),
            algorithm=SHA256(),
            label=None
        )
    )
    return decrypted.decode()