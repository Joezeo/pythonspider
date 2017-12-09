# coding=UTF-8
import urllib.request


class HtmlDownloader:
    def download(self, url):
        if url is None:
            return
        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return
        return response.read()
