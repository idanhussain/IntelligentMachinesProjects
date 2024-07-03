import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256


def decrypt_data(encrypted_text, private_key_pem):
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(),
        password=None,
    )

    decrypted = private_key.decrypt(
        encrypted_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None
        ),
    )
    return decrypted.decode()


# Private key in PEM format
private_key_pem = """
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

# Encrypted text (base64 encoded string)
encrypted_text_base64 = "Na7WDBmiarTRrRcJcETxb6HUqIe8ke3nNX1ILNpfeEU/lu0rF5A1zdKt0wt6BpH221AT64gB7sb6qmmA7W9TvQY5AwoYEPT4nMkKDxLuBh0SYDPPjzRA6etKormH/2aCD2RV1cLp3kJRDt/X27+GyrmqFXtutHNEEiFXF9hoU49K//JR2OyF4qaxpgFgd+DB2yhGnrmSiNl4blJABxgCHLVhrILT5OfWuEHUq4o2u05+pEg1J+ORklx9x8kR2RoaLhF23iSuEwMNQlJ+4OaZF3UMXZR1h8hepbul4VwL+DLU+wQQv/+f/I2ZKjxOoH2WK5RiJChCjUnw6gmO4RvVgA=="

# Decode the base64 encoded string to bytes
encrypted_text = base64.b64decode(encrypted_text_base64)

# Decrypt the encrypted text
try:
    decrypted_message = decrypt_data(encrypted_text, private_key_pem)
    print("Decrypted message:", decrypted_message)
except Exception as e:
    print("An error occurred:", str(e))
