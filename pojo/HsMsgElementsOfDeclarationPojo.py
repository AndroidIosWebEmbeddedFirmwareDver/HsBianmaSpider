# 申报要素实体类
class HsMsgElementsOfDeclarationPojo:

    # 构造函数
    def __init__(self):
        # print('-init-')
        # 商品编码
        self.productElementsOfDeclaration: [] = []

    # 析构函数
    def __del__(self):
        # print('-del-')
        # 商品编码
        self.productElementsOfDeclaration: [] = None
