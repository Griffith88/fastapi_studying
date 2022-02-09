from passlib.context import CryptContext

pass_crypt_context = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pass_crypt_context.hash(password)

    @staticmethod
    def verify(hashed_password: str, plain_password: str) -> bool:
        return pass_crypt_context.verify(plain_password, hashed_password)
