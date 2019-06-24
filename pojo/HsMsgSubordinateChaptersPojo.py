
from pojo.HsMsgSubordinateChaptersChapterPojo import HsMsgSubordinateChaptersChapterPojo


# 所属章节实体类
class HsMsgSubordinateChaptersPojo:

    # 构造函数
    def __init__(self):
        # print('-init-')
        self.chapters: [HsMsgSubordinateChaptersChapterPojo] = []

    # 析构函数
    def __del__(self):
        # print('-del-')
        self.chapters: [HsMsgSubordinateChaptersChapterPojo] = None
