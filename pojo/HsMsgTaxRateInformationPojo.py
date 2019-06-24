# 获取税率信息实体类
class HsMsgTaxRateInformationPojo:

    # 构造函数
    def __init__(self):
        # print('-init-')
        # 计量单位
        self.productUnitOfMeasurement = None
        # 出口税率
        self.productExportTariffRate = None
        # 出口退税税率
        self.productExportTaxRebateRate = None
        # 出口暂定税率
        self.productExportTemporaryTaxRate = None
        # 增值税率
        self.productExportVATRate = None
        # 进口优惠税率
        self.productExportImportPreferentialTaxRate = None
        # 进口暂定税率
        self.productImportTemporaryTaxRate = None
        # 进口普通税率
        self.productImportCommonTaxRate = None
        # 消费税率
        self.productConsumptionTaxRate = None

    # 析构函数
    def __del__(self):
        # print('-del-')
        # 计量单位
        self.productUnitOfMeasurement = None
        # 出口税率
        self.productExportTariffRate = None
        # 出口退税税率
        self.productExportTaxRebateRate = None
        # 出口暂定税率
        self.productExportTemporaryTaxRate = None
        # 增值税率
        self.productExportVATRate = None
        # 进口优惠税率
        self.productExportImportPreferentialTaxRate = None
        # 进口暂定税率
        self.productImportTemporaryTaxRate = None
        # 进口普通税率
        self.productImportCommonTaxRate = None
        # 消费税率
        self.productConsumptionTaxRate = None
