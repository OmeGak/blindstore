def generate_keypair():
    raise NotImplementedError()


class PublicKey(object):
    def encrypt(self, plaintext):
        raise NotImplementedError()


class SecretKey(object):
    def decrypt(self, ciphertext):
        raise NotImplementedError()


class Ciphertext(object):
    def __getitem__(self, i):
        raise NotImplementedError()

    def __setitem__(self, i, value):
        raise NotImplementedError()

    def __next__(self):
        raise NotImplementedError()
    next = __next__

    def __iter__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __xor__(self, other):
        raise NotImplementedError()
    __add__ = __xor__

    def __and__(self, other):
        raise NotImplementedError()
    __mul__ = __and__
