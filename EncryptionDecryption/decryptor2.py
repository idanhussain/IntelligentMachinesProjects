from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.hashes import SHA256

# Generate a new RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()

# Serialize the private key to PEM format
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

# Serialize the public key to PEM format
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)


# Encrypt data using the public key
def encrypt_data(public_key, data):
    encrypted = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None
        ),
    )
    return encrypted


# Decrypt data using the private key
def decrypt_data(encrypted_text, private_key_pem):
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=None,
    )

    decrypted = private_key.decrypt(
        encrypted_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None
        ),
    )
    return decrypted.decode()


# Data to be encrypted
data = "This is a secret message"

# Encrypt the data
encrypted_text = encrypt_data(public_key, data)
print("Encrypted text:", encrypted_text)

# Decrypt the data
try:
    decrypted_message = decrypt_data(encrypted_text, pem_private_key)
    print("Decrypted message:", decrypted_message)
except Exception as e:
    print("An error occurred:", str(e))
