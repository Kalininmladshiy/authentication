import hashlib
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher


class BCryptSHA512PasswordHasher(BCryptSHA256PasswordHasher):
    algorithm = "bcrypt_sha512"
    digest = hashlib.sha512
