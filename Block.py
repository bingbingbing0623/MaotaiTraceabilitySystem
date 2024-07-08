import hashlib
import json
from datetime import datetime
from Transaction import Transaction, TransactionEncoder


class Block:
    """
    区块结构
        prev_hash:      父区块哈希值
        transactions:   交易对
        timestamp:      区块创建时间
        hash:           区块哈希值
        nonce:          随机数
    """

    def __init__(self, transactions, prev_hash):
        # 将传入的父哈希值和数据保存到类变量中
        self.prev_hash = prev_hash
        # 交易列表
        self.transactions = transactions
        # 获取当前时间
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 设置Nonce和哈希的初始值为None
        self.nonce = None
        """
        计算区块的哈希值
        """
        # 获取哈希对象
        message = hashlib.sha256()
        # 先将数据内容转为字符串并进行编码，再将它们哈希
        # 注意：update() 方法现在只接受 bytes 类型的数据，不接收 str 类型
        message.update(str(self.prev_hash).encode('utf-8'))
        message.update(str(self.prev_hash).encode('utf-8'))
        message.update(str(self.prev_hash).encode('utf-8'))
        # update() 更新 hash 对象，连续的调用该方法相当于连续的追加更新
        # 返回字符串类型的消息摘要
        self.hash = message.hexdigest()

    # 类的 __repr__() 方法定义了实例化对象的输出信息
    def __repr__(self):
        return f"父哈希值：{self.prev_hash}\n区块内容：{self.transactions}\n区块哈希值：{self.hash}"  # 添加父哈希值的显示
        


 
 
