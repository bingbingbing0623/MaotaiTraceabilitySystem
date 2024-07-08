from Block import Block
from Transaction import Transaction
from Wallet import Wallet, verify_sign
 
 
class BlockChain:
    """
        区块链结构体
            blocks:        包含的区块列表
    """
 
    def __init__(self):
        self.blocks = []
 
    def add_block(self, block):
        """
            添加区块
        """
        self.blocks.append(block)
 
    def print_list(self):
        print(f"区块链包含个数为：{len(self.blocks)}")
        for block in self.blocks:
            print(f"区块父哈希值为：{block.prev_hash}")
            print(f"区块内容为：{block.transactions}")
            print(f"区块哈希值为：{block.hash}")
            print(f"\n")
        print()

    def find_batch_details(self, batch_id):
        """
            查询指定批次号的茅台酒详情
        """
        for block in self.blocks:
            for transaction in block.transactions:
                if transaction.batch_id == batch_id:
                    print(f"生产厂商信息：{producer.address}")
                    return transaction.details
        return "未找到该批次茅台酒的详情"
    
    def find_trans_details(self, trans,batch_id):    
        """
        查询指定交易的茅台酒详情
        """
        for block in self.blocks:
            for transaction in block.transactions:
                if transaction.batch_id == batch_id:
                    if transaction.trans == trans:
                        return f"交易存在，茅台酒详情为：{transaction.details}"
        return "交易不存在"
    




# 传入用户和区块链，返回用户的“余额”和总余额
def get_balance(user, blockchain):
    balance = user.balance
    total_balance = user.balance  # 添加总余额变量
    for block in blockchain.blocks:
        for t in block.transactions:
            if t.sender == user.address.decode():
                balance -= t.amount
            elif t.recipient == user.address.decode():
                balance += t.amount
            total_balance += t.amount  # 计算总余额
    return balance, total_balance  # 返回用户余额和总余额


# 新建交易列表
transactions = []
 
# 创建 3 个用户
producer = Wallet()  # 茅台酒生产商
consumer1 = Wallet()  # 茅台酒消费者1
consumer2 = Wallet()  # 茅台酒消费者2
 
print("茅台酒生产商创建创世区块...")
blockchain = BlockChain()
print()
 
print(f"茅台酒生产商的余额为 {get_balance(producer, blockchain)[0]} 元")
print(f"消费者1的余额为 {get_balance(consumer1, blockchain)[0]} 元")
print(f"消费者2的余额为 {get_balance(consumer2, blockchain)[0]} 元")
print()


# 打印区块链信息
blockchain.print_list()
 ############################################################
 #新增交易
print("新增交易：生产商生产一批茅台酒")
batch_details = "2024年5月生产的茅台酒，批次号: 12345"
nt = Transaction(
    sender=producer.address,
    recipient=producer.address,
    amount=10,  # 生产商获得10茅台酒
    batch_id="12345",
    details=batch_details
)
transactions.append(nt)
print(f"新增茅台酒生产信息：{batch_details}")
print()

blockchain.add_block(Block(transactions=transactions, prev_hash=""))

# 打印区块链信息
blockchain.print_list()
#################################################################
#新增交易
print("新增交易：生产商生产第二批茅台酒")
batch_details = "2024年6月生产的茅台酒，批次号: 111111"
nt = Transaction(
    sender=producer.address,
    recipient=producer.address,
    amount=10,  # 生产商获得10茅台酒
    batch_id="111111",
    details=batch_details
)
transactions.append(nt)
print(f"新增茅台酒生产信息：{batch_details}")
print()

blockchain.add_block(Block(transactions=transactions, prev_hash=blockchain.blocks[-1].hash))

# 打印区块链信息
blockchain.print_list()


#################################################################
#新增交易
print("新增交易：消费者1买了5瓶茅台酒")
batch_details = "2024年6月生产的茅台酒，批次号: 111111,交易号：01,一共购买5瓶茅台。"
nt = Transaction(
    sender=producer.address,
    recipient=consumer1.address,
    amount=5,  # 消费者获得5茅台酒
    batch_id="111111",
    trans="01",
    details=batch_details
)
transactions.append(nt)
print(f"新增茅台酒销售信息：{batch_details}")
print()

blockchain.add_block(Block(transactions=transactions, prev_hash=blockchain.blocks[-1].hash))

# 打印区块链信息
blockchain.print_list()





######################################
#查询批次号
while True:
    # 获取用户输入的批次号
    batch_id = input("请输入批次号：")

    # 查询批次号对应的茅台酒详情
    details = blockchain.find_batch_details(batch_id)

    # 打印查询结果
    if details:
        print(f"批次号为 {batch_id} 的茅台酒详情：\n{details}\n")
        # 获取用户输入的批次号
        while True:
            # 获取用户输入的批次号
            trans = input("请输入交易号：")

            # 查询批次号对应的茅台酒详情
            trans = blockchain.find_trans_details(trans,batch_id)
            print(f"{trans}")

            # 询问用户是否继续查询
            choice = input("是否继续查询交易？(Y/N): ")
            if choice.lower() == "n":
                break


    # 询问用户是否继续查询
    choice = input("是否继续查询茅台酒批次？(Y/N): ")
    if choice.lower() == "n":
        break


