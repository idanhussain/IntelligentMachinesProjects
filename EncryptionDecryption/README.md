# RSA Encryptor and Decryptor 
## Introduction
This code provides a simple implementation of RSA encryption and decryption in both JavaScript and Python. The JavaScript module encryptor.js allows you to encrypt strings using a public RSA key, while the Python decryptor.py allows you to decrypt the encrypted data using the corresponding private RSA key. This encryptor can be integrated into web applications to secure sensitive data transmission.

## Libraries
- [js-encrypt](https://www.npmjs.com/package/jsencrypt):
A JavaScript library for RSA encryption and decryption. It supports key generation, encryption, and decryption.

- [cryptography](https://cryptography.io/en/latest/):
A Python library that provides cryptographic recipes and primitives. It includes support for RSA encryption and decryption.

## Usage
### generate_keys.py
Run the generate_keys.py script to generate a new RSA key pair. The generated keys will be saved as private_key.pem and public_key.pem.
```bash
python generate_keys.py
```

### encryptor.js
Call the **encryptString** function to return the encrypted text. The function takes in two parameters: the string to be encrypted, and the public key.
```javascript
const publicKey = `-----BEGIN PUBLIC KEY-----
...
-----END PUBLIC KEY-----`;

const encrypted = encryptString("This string will be encrypted", publicKey);
```

### decryptor.py
Call the **decrypt_string** function to return the decrypted text. The function takes in two parameters: the encrypted text to be decrypted, and the private key PEM. This function uses PKCS#1 v1.5 padding to match JSEncrypt's encryption format.
```python
encrypted_text = "encrypted text generated from encryptor.js"

private_key = """-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----"""

decrypted_message = decrypt_data(encrypted_text, private_key)
```

_Note: The method in which the keys will be read depends on the specific implementation of this encryptor._

## Testing 
### encryptor.test.js
The JavaScript tests use the Jest testing framework. The tests verify the following:
- Encryption of data is successful.
- Errors are thrown for null, undefined, and non-string inputs.
- Unique encryptions are generated for identical strings.
  
Run the tests:

```bash
npm test
```

### decryptor_test.py
The Python tests use the pytest testing framework. The tests verify the following:
- Decryption of data is successful.
- Different encrypted texts for the same message result in the same decrypted message.
- Errors are raised for invalid keys and invalid encrypted texts.

Run the tests:
```bash
pytest decryptor_test.py
```

## Authors and Acknowledgement
Code written by Idan Hussain and Edaad Azman.
