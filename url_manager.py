# coding=UTF-8


class UrlManager:
    """Manager模块初始化
    Manager模块主要功能是使用集合，对待爬取，和已爬取的url进行管理
    """
    def __init__(self):
        """Manager模块初始化
        创建 待爬取url 和 已爬取url集合
        """
        self.new_urls = set()   # 待爬取的url
        self.old_urls = set()   # 已爬取的url

    def add_new_url(self, url):
        """Manager模块函数
        如果新的url不在 待爬取url 和 已爬取url 中
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """Manager模块接口函数
        添加一组urls,使用add_new_url方法进行url的添加
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        """Manager模块接口函数
        判断待爬取url是否为空
        """
        return len(self.new_urls) != 0

    def get_new_url(self):
        """Manager模块接口函数
        从待爬取的url中取出一条url，使用Downloader模块进行下载
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
