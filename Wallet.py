import hashlib
import base58
import binascii
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes

class Wallet:
    """
    钱包
    """

    def __init__(self):
        """
        钱包初始化时基于椭圆曲线生成一个唯一的秘钥对，代表区块链上一个唯一的账户
        """
        # 生成私钥
        self._private_key = ec.generate_private_key(ec.SECP256K1)
        # 基于私钥生成公钥
        self._public_key = self._private_key.public_key()
        self.balance = 10000

    @property
    def address(self):
        """
        这里通过公钥生成地址
        """
        public_key_bytes = self._public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        # 使用RIPEMD160哈希算法对公钥进行哈希
        h = hashlib.new('ripemd160')
        h.update(public_key_bytes)
        # 对哈希结果进行Base58编码生成地址
        return base58.b58encode(h.digest())

    @property
    def pubkey(self):
        """
        返回公钥字符串
        """
        return self._public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def sign(self, message):
        """
        生成数字签名
        """
        h = hashlib.sha256(message.encode('utf8')).digest()
        # 利用私钥生成签名
        signature = self._private_key.sign(
            h,
            ec.ECDSA(hashes.SHA256())
        )
        return signature

def verify_sign(pubkey, message, signature):
    """
    验证签名
    """
    public_key = serialization.load_pem_public_key(
        pubkey,
        backend=default_backend()
    )
    h = hashlib.sha256(message.encode('utf8')).digest()
    try:
        public_key.verify(
            signature,
            h,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except:
        return False

