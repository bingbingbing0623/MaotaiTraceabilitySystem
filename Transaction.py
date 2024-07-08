import json
 
 
class Transaction:
    """
        交易的结构
    """
 
    def __init__(self, sender, recipient, amount, batch_id=None, details=None,trans=None):
        """
            初始化交易，设置交易的发送方、接收方、交易数量以及茅台酒的批次号和详情
        """
        self.pubkey = None  # 交易发送者的公钥
        self.signature = None  # 交易的数字签名
        self.sender = sender  # 发送方
        self.recipient = recipient  # 接收方
        self.amount = amount  # 交易数量
        self.batch_id = batch_id  # 茅台酒的批次号
        self.details = details  # 茅台酒的详情
        self.trans = trans  # 茅台酒的详情
 
    def set_sign(self, signature, pubkey):
        """
            设置交易的签名和公钥
        """
        self.signature = signature  # 签名
        self.pubkey = pubkey  # 发送方公钥
 
    def __repr__(self):
        """
            打印交易信息，包括发送方、接收方、交易数量以及茅台酒的批次号和详情
        """
        if self.sender:
            s = f"从{self.sender}向{self.recipient}转移{self.amount}瓶茅台酒，茅台酒批次号为{self.batch_id}，详情为{self.details}"
        else:
            s = "error"
        return s




class TransactionEncoder(json.JSONEncoder):
    """
        定义Json的编码类，用来序列化Transaction
    """
    def default(self, obj):
        if isinstance(obj, Transaction):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)
            # return super(TransactionEncoder, self).default(obj)