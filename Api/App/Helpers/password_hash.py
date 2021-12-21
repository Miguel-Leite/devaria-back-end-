from hashlib import blake2b
from hmac import compare_digest


class SecretPassword:

    SECRET_KEY = b'password_hashSecretKey'
    AUTH_SIZE = 20

    @classmethod
    def password_encrypt(cls, password: str):
        """ encrypt password"""

        if password != "":

            hash_blake = blake2b(digest_size=cls.AUTH_SIZE, key=cls.SECRET_KEY)
            hash_blake.update(password.encode())
            return hash_blake.hexdigest().encode('utf-8')

    @classmethod
    def password_verify(cls, password: str, hash_password: bytes):
        """ verify valid password"""

        password_genr = cls.password_encrypt(password)

        if not compare_digest(password_genr, hash_password):
            return False

        return True
