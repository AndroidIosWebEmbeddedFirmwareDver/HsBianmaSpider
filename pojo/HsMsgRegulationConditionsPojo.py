# 申报要素实体类
class HsMsgRegulationConditionsPojo:

    # 构造函数
    def __init__(self):
        # print('-init-')
        # 监管条件
        self.productRegulationConditions: [] = []

    # 析构函数
    def __del__(self):
        # print('-del-')
        # 监管条件
        self.productRegulationConditions: [] = None
