import bcrypt


class PasswordHasher:
    def hash(self, password: str):
        salt = bcrypt.gensalt(12)
        hash = bcrypt.hashpw(password.encode(encoding="utf-8"), salt)

        return hash, salt
