const encryptData = require("./encryptor.js"); // Adjust the path if necessary
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

test("encryptData function encrypts data correctly", () => {
  const data = encryptAndSend();
  const encryptedData = encryptData(data);

  // Check if the encrypted data is not null or undefined
  expect(encryptedData).not.toBeNull();
  expect(encryptedData).toBeDefined();

  // Check if the encrypted data is a string
  expect(typeof encryptedData).toBe("string");

  // Additional checks could include the length of the encrypted string or specific patterns
  // Note: Exact matching with encrypted data is generally not useful because encryption results vary
  expect(encryptedData.length).toBeGreaterThan(0);
});
