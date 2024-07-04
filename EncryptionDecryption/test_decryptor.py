import pytest
from decryptor import decrypt_data

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

expected_decrypted_text = "This is the original message."

encrypted_text_1 = """
SCeBkSJMlIgDxYNWGrfRKa4CKRkN33oTg8K+JY8L4K96hs/+gCXOd7BRS25zJ/56q1Xf9hNrPLeQSvWMWx8aI/DpvDwZepjJA8f57OZw6o4A1TN8Mx2ObDo9RCnWEiYjT86ZZ2gIGaImlGk2g0TU+URqv/sNfR5phd3TL8zlirJ4XFW5zYlU8t3BcMvSFPHR0wHhH4Fy8t9XSXfje2wVE08fSyCMblZt6zfNgI3C6OuyI6C/ljglk5nMFJZzpMzSFp8E+qLO+o24nSUJ5HDyCApm3uHiWUcMF0pYHbG/E35UYCd9+4L2DGTJoX+aECltizFwAFEoI4zB2HHExmoeYw==
"""

encrypted_text_2 = """
AwQqgYtQXbXGZJHodZh1BszofdP9ysMqKSf1UaeNsW/sybjdLwOJu4cep46MIXPd4RuHOk96+vRMS6JZN9u6d4PtKkKnTU9gTzlZ2kF/BAjeH2l3iP47CW86vL5SB0V11mqHQI7mWM99oaJguAodD3dvqiIADiGjypm9Uvj8MOma4hzqQ4K2RnB41wEVd9GOa6No9ULslw7gt5DIspdMeMv3GJa0wLBv1Y1KrEpgDpTuOO/eJ62I+4O5ydp2HejQWDVunIrywuLGZV0Lvm7THWYkVxM0zBfuBXEsMZ5lQ/y22uF54hSu5Zga3ZeskVpF4gIXNuOrbtm4OdzM3etLqA==
"""


def test_decrypt_data_success():
    decrypted_message = decrypt_data(encrypted_text_1, pem_private_key)
    assert decrypted_message == expected_decrypted_text


def test_different_encrypted_text_same_message():
    decrypted_message_1 = decrypt_data(encrypted_text_1, pem_private_key)
    decrypted_message_2 = decrypt_data(encrypted_text_2, pem_private_key)
    assert decrypted_message_1 == decrypted_message_2


def test_decrypt_data_invalid_key():
    invalid_pem_private_key = "invalid key"
    with pytest.raises(ValueError):
        decrypt_data(encrypted_text_1, invalid_pem_private_key)


def test_decrypt_data_invalid_encrypted_text():
    invalid_encrypted_text = "invalid encrypted text"
    with pytest.raises(ValueError):
        decrypt_data(invalid_encrypted_text, pem_private_key)


pytest.main()
