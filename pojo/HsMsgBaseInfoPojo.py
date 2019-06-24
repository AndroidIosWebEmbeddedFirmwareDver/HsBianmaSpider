# 基本信息实体类
class HsMsgBaseInfoPojo:

    # 构造函数
    def __init__(self):
        # print('-init-')
        # 商品编码
        self.productName = None
        # 商品名称
        self.productCode = None
        # 编码状态
        self.productCodeStatus = None
        # 更新时间
        self.productUpdateTime = None

    # 析构函数
    def __del__(self):
        # print('-del-')
        # 商品编码
        self.productName = None
        # 商品名称
        self.productCode = None
        # 编码状态
        self.productCodeStatus = None
        # 更新时间
        self.productUpdateTime = None
