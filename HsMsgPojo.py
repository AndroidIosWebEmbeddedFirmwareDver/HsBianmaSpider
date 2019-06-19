from HsMsgBaseInfoPojo import HsMsgBaseInfoPojo


class HsMsgPojo:
    msgName = ''
    baseInfo = ''

    #
    # def __init__(self):
    #     print('-init')

    def __init__(self):
        """Constructor
        """
        print('-init')

    def __del__(self):
        print('-del')

    def getMsgName(self):
        return self.msgName

    def getBaseInfo(self):
        return self.baseInfo

    def setMsgName(self, msgName):
        self.msgName = msgName

    def setBaseInfo(self, baseInfo: HsMsgBaseInfoPojo):
        self.baseInfo = baseInfo
