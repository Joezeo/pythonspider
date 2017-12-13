# coding=UTF-8
import urllib.request


class HtmlDownloader:
    def download(self, url):
        """Downloader接口函数
        从url下载取得页面信息，并返回所取得的信息
        """
        if url is None:
            return
        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return
        return response.read()
