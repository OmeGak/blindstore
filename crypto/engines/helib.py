def generate_keypair():
    raise NotImplementedError()


class PublicKey(object):
    def encrypt(self, plaintext):
        raise NotImplementedError()


class SecretKey(object):
    def decrypt(self, ciphertext):
        raise NotImplementedError()
