# Imports
from cryptography.hazmat.primitives import hashes;
from cryptography.hazmat.backends import default_backend;
from cryptography.hazmat.primitives.asymmetric import rsa;
from cryptography.hazmat.primitives.asymmetric import padding;

# Functions
def createRSAKeyPair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key();

    return (public_key, private_key);

def createPadding():
    return padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )

def encrypt(content, key):
    return key.encrypt(content.encode(), createPadding());

def decrypt(encrypted, key):
    return key.decrypt(encrypted, createPadding()).decode();