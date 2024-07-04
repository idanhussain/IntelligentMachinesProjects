const encryptString = require("./encryptor.js");
const forge = require("node-forge");
const fs = require("fs");
const path = require("path");

// Load the public key
const publicKeyPem = `-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApbDipQkCbHohE76Fnw1i
hRkLdQdZZepRWYLd9PsdGaG9kxLf+JLda/faz7g7ApKc4UvQCBKGNI4UIuXpFiGz
x6C/E3vx4ziJGlRnbfxz1Rl0b9+OZAfMebhz+PJ7u4ZK6d0nd2yEXExNiUWvWy3x
euQf0k89r+CACgdw/dOsEwhVLp2+v+mcNlRjiQcIIwbKhRbDvc7/3c/N7fhIZu8F
dzZ41c4yS3f/10rB2Rsle4dsL+o6Bshb98Hj5vxebmRWenyA6GqsDi4O/IQdmFEM
oeYe0ql6vToxnMOHJttanU4fAEiXLrjknm1WlbXoDx0os9LlvRO0EeDe6mywxnGM
+QIDAQAB
-----END PUBLIC KEY-----`;

test("encryptString function encrypts data correctly", () => {
  const encryptedData = encryptString("data", publicKeyPem);

  expect(encryptedData).not.toBeNull();
  expect(encryptedData).toBeDefined();

  expect(typeof encryptedData).toBe("string");

  expect(encryptedData.length).toBeGreaterThan(0);
});
