const encryptString = require("./encryptor.js");

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

test("encryptString function encrypts data successfully", () => {
  const testEncryption = encryptString("test string", publicKeyPem);

  expect(testEncryption).not.toBeNull();
  expect(testEncryption).toBeDefined();
  expect(typeof testEncryption).toBe("string");
  expect(testEncryption.length).toBe(344);
});

test("encryptString function throws error for null input", () => {
  expect(() => {
    encryptString(null, publicKeyPem);
  }).toThrow("Input is null or undefined");
});

test("encryptString function throws error for undefined input", () => {
  expect(() => {
    encryptString(undefined, publicKeyPem);
  }).toThrow("Input is null or undefined");
});

test("encryptString function throws error for non-string input", () => {
  expect(() => {
    encryptString(1000, publicKeyPem);
  }).toThrow("Input is not a string");
});

test("encryptString function generates unique encryptions for indentical strings", () => {
  const identicalEncryptionTest1 = encryptString("indentical string", publicKeyPem);
  const identicalEncryptionTest2 = encryptString("indentical string", publicKeyPem);

  expect(identicalEncryptionTest1).not.toBe(identicalEncryptionTest2);
});
