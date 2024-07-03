import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256


# Decrypt data using the private key
def decrypt_data(encrypted_text, private_key_pem):
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(),
        password=None,
    )

    decrypted = private_key.decrypt(
        base64.b64decode(encrypted_text),
        padding.PKCS1v15(),  # Use PKCS#1 v1.5 padding to match JSEncrypt
    )
    return decrypted.decode()


# Private key in PEM format
pem_private_key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEApbDipQkCbHohE76Fnw1ihRkLdQdZZepRWYLd9PsdGaG9kxLf
+JLda/faz7g7ApKc4UvQCBKGNI4UIuXpFiGzx6C/E3vx4ziJGlRnbfxz1Rl0b9+O
ZAfMebhz+PJ7u4ZK6d0nd2yEXExNiUWvWy3xeuQf0k89r+CACgdw/dOsEwhVLp2+
v+mcNlRjiQcIIwbKhRbDvc7/3c/N7fhIZu8FdzZ41c4yS3f/10rB2Rsle4dsL+o6
Bshb98Hj5vxebmRWenyA6GqsDi4O/IQdmFEMoeYe0ql6vToxnMOHJttanU4fAEiX
Lrjknm1WlbXoDx0os9LlvRO0EeDe6mywxnGM+QIDAQABAoIBAG2jXHXkPkxVjCmq
enTCwJxd9CzeThOYN3hJlmGTALCDTBRT+wxa8lWNTqcAu1t6dIDIT8HnsBJ6qWxm
QhQ4/ONtxMI509eNA3v+ueoXkPZDv75/aZNbbbxlh6gFnEZ8GHojswfdMMB6ZRwe
lmh5QD8XUM8zTBhjL5ZzUhtDw6tbWTC7qm5GcD6PjhjZLJcr3AGh5GdhFzhScSRM
0yrpoHiBYX+NQlZUsGA5xPERBBNyHAMTzOYHOFMFJqfp7PetQ73kRTb80va3tofn
rmnmJkCAa863xLCuP2+aWFxZY4ZlO8ip/Q/PMY7Zi51SfDD650yzGrinssFtld2C
vYcFHTkCgYEA2gYVSJ2mLmOrMwa4qwt/OiY6GbaDGdmKogewK/5WWnJ/jx7NveHg
9B9WRYjUXd4NO2fK4L8MVpNXJ5Jy0L2uNev5CQJLDgXFCJ+/Oaott39Cy/KOQL/Q
xsZbuheKSEaLoGu5zvWy4i5y9HvlTV55J8ZC0mzRSUfWj/wM+85LGB8CgYEAwo05
upye5AkK8XvOFumBVcEdusAzaIduMLxebamQEJO3LDQWRhYToqu/CuVDRDfSh6WW
79Bbv7iEgtmXzHe7Ym4Xxl6DlUZwAcWcA7Ewiwo01jpGZP+OFmwKyizJgqS5rIgg
ecsgkOfv7oWklKv+hbS/Yy+Ql2MxJN63An38F+cCgYA70++DPb+cez0/g1iplz4S
dur6o1rWfRvN2s49RE3uA/19CLbspE9WrkK+Ug30tDptUs4ZXlPEbio8cbOQFHz5
zwdHsZlm/65R74RKDqj88a8iyCzBF+HyqfwB1PPdYX5vRyB16nZsGtLwxA7obERS
5dTwaWwE7/GxETl+3907gQKBgCGjDz8fgy1EDvtPf4Ngnfb4q641Ou4wtDGC8ASf
04O6NmpTGyLFAGIYtbApkWbDDAhd7enKqYJNYcPJ4T/9140eIcgvYSq3AficdOwC
f7Uab6Y2byNZN/TSe08XTUPkPSICazMDlr7XCxm/S4RU9G2joY+BkstJ4B5Sz2uD
4skzAoGBALBeb9kROaZCfxzgFV5RnxW7VvNtwqWOa2cKxtz1PDKo0w8IstPQjwvz
cuzhJaMBI2eoCOIaUGRlZCCYOyd1U4k2CZgvI/8XGiuwZPX0djNOeiORGaTr6I3v
nvfkZ6PMsPqhTEtOkcIA4CDoqKFxoSBrR16xcigBv8cnFHOw8gof
-----END RSA PRIVATE KEY-----
"""

# Encrypted text (from JavaScript output)
encrypted_text = "j5Fqe4OckbC0JYzZC8nmB5adNrL9RmOJtfCRvr8jmSlhNwtEuDDaE8fm5BRux0SyO/jBkiI8rxJp2hhVL/6nNF4/M9iDoy6YrmtpAY/akP5l0iMy6/H4qJb5URAnrj6knMIOaAPQhKcgfP823Ww40TOprJjkD+130e6CcYhN+kSOfZ7i2EaY/k8DoExUvmv9JsqPuo7kzkfCId9WdBMmdKxwnXcGKfXqUdzw0OsSWy1QlAF5vJp3Hrz6vgLSg/YGuSbz0AKr+Uz9W7XG6YyduG31XmApkcVHbowmruypqU8Kh01d+dLmOZ2dRNEXIe9tLXUIGTN094pY7jzcoRLx3w=="

# Decrypt the data
try:
    decrypted_message = decrypt_data(encrypted_text, pem_private_key)
    print("Decrypted message:", decrypted_message)
except Exception as e:
    print("An error occurred:", str(e))
