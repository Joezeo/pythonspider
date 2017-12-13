# coding=UTF-8
import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain:
    def __init__(self):
        """初始化
        建立四个模块的实例
        """
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        """爬虫程序的主函数
        程序主逻辑函数
        """
        count = 1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw: {} : {}".format(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break
                count += 1
            except Exception:
                print('craw failed!')
        self.outputer.output()


if __name__ == '__main__':
    # 根url，爬虫程序爬取网页的起点
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
