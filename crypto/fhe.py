engine = __import__('engines.helib')


def generate_keypair():
    pk, sk = engine.generate_keypair()
    return PublicKey(pk), SecretKey(sk)


class PublicKey(object):
    def __init__(self, raw_key):
        self._raw = raw_key

    def __str__(self):
        return str(self._raw)

    @staticmethod
    def deserialize(serialized_key):
        raw_key = engine.PublicKey.deserialize(serialized_key)
        return PublicKey(raw_key)

    def encrypt(self, plaintext):
        return self._raw.encrypt(plaintext)


class SecretKey(object):
    def __init__(self, raw_key):
        self._raw = raw_key

    def __str__(self):
        return str(self._raw)

    @staticmethod
    def deserialize(serialized_key):
        raw_key = engine.SecretKey.deserialize(serialized_key)
        return SecretKey(raw_key)

    def decrypt(self, ciphertext):
        return self._raw.decrypt(ciphertext)


class Ciphertext(object):
    def __init__(self, string):
        self._raw = engine.Ciphertext(string)
