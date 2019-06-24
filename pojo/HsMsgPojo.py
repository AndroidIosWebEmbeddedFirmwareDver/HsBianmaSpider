from pojo.HsMsgBaseInfoPojo import HsMsgBaseInfoPojo
from pojo.HsMsgTaxRateInformationPojo import HsMsgTaxRateInformationPojo
from pojo.HsMsgElementsOfDeclarationPojo import HsMsgElementsOfDeclarationPojo
from pojo.HsMsgRegulationConditionsPojo import HsMsgRegulationConditionsPojo
from pojo.HsMsgInspectionAndQuarantineCategoriesPojo import HsMsgInspectionAndQuarantineCategoriesPojo
from pojo.HsMsgSubordinateChaptersPojo import HsMsgSubordinateChaptersPojo
from pojo.HsMsgCIQCodePojo import HsMsgCIQCodePojo
from pojo.HsMsgNaviHtmlPojo import HsMsgNaviHtmlPojo


# 编码信息实体类
class HsMsgPojo:

    def __init__(self):
        # 基本信息
        self.baseInfo: HsMsgBaseInfoPojo = None
        # 税率信息
        self.taxRateInfo: HsMsgTaxRateInformationPojo = None
        # 申报要素
        self.elementDeclar: HsMsgElementsOfDeclarationPojo = None
        # 监管条件
        self.regulCondition: HsMsgRegulationConditionsPojo = None
        # 检验检疫类别
        self.inspAndQuartCate: HsMsgInspectionAndQuarantineCategoriesPojo = None
        # 所属章节
        self.chapters: HsMsgSubordinateChaptersPojo = None
        # CIQ编码
        self.ciq: HsMsgCIQCodePojo = None
        # 导航信息
        self.naviHtmls: [HsMsgNaviHtmlPojo] = None

    def __del__(self):
        # 基本信息
        self.baseInfo: HsMsgBaseInfoPojo = None
        # 税率信息
        self.taxRateInfo: HsMsgTaxRateInformationPojo = None
        # 申报要素
        self.elementDeclar: HsMsgElementsOfDeclarationPojo = None
        # 监管条件
        self.regulCondition: HsMsgRegulationConditionsPojo = None
        # 检验检疫类别
        self.inspAndQuartCate: HsMsgInspectionAndQuarantineCategoriesPojo = None
        # 所属章节
        self.chapters: HsMsgSubordinateChaptersPojo = None
        # CIQ编码
        self.ciq: HsMsgCIQCodePojo = None
        # 导航信息
        self.naviHtmls: [HsMsgNaviHtmlPojo] = None
