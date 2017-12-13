# coding=UTF-8
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParser:
    """parser模块
    对downloader模块下载下来的网页信息进行分析处理
    """
    def _get_new_urls(self, page_url, soup):
        """Parser模块函数
        从当前url获得新的urls，并返回获得的urls
        """
        new_urls = set()
        # <a target="_blank" href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7
        #%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80">计算机程序设计语言</a>
        links = soup.find_all('a', href=re.compile(r"/item/[a-zA-Z0-9%]+"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """Parser模块函数
        从当前url获得页面数据，并返回取得的数据
        """
        res_data = {}
        # url:
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-\
lemmaTitle-title").find('h1')

        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        """Parser模块接口函数
        调用模块的_get_new_urls和_get_new_data函数从当前page_url获得链接和数据
        """
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='GB2312')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
