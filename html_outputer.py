# coding=UTF-8


class HtmlOutputer:
    """Outputer模块
    对从parser模块取得的数据，进行输出到html文件的处理
    """
    def __init__(self):
        """outputer初始化
        建立一个存放数据的列表
        """
        self.datas = []

    def collect_data(self, data):
        """outputer模块接口函数
        收集数据，并将其放入datas列表中
        """
        if data is None:
            return
        self.datas.append(data)

    def output(self):
        """outputer模块接口函数
        输出函数，将datas列表中的数据输出到列表中
        """
        fout = open('..\\tmp\\output.html', 'w')
        fout.write('<html>\n')
        fout.write('<body>\n')
        fout.write('<table>\n')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>{}</td>'.format(data['url'].encode('UTF-8')))
            fout.write('<td>{}</td>'.format(data['title'].encode('UTF-8')))
            fout.write('<td>{}</td>'.format(data['summary'].encode('UTF-8')))
            fout.write('</tr>')

        fout.write('\n</table>')
        fout.write('\n</body>')
        fout.write('\n</html>')
        fout.close()
