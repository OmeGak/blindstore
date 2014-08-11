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
    def __init__(self, serialized_ciphertext):
        self._raw = engine.Ciphertext(serialized_ciphertext)

    def __getitem__(self, i):
        return self._raw[i]

    def __setitem__(self, i, value):
        self._raw[i] = value

    def __next__(self):
        self._raw.__next__()
    next = __next__

    def __iter__(self):
        self._raw.__iter__()

    def __len__(self):
        self._raw.__len__()

    def __xor__(self, other):
        self._raw.__xor__(other)
    __add__ = __xor__

    def __and__(self, other):
        self._raw.__and__(other)
    __mul__ = __and__
