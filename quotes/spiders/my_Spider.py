import scrapy
import quotes.items
import json
import re
class MySpider(scrapy.Spider):
    name = "wangyiyun"
    allowed_domains = ["music.163.com"]
    str = input("输入客户端分享的链接：")
    # str = "http://music.163.com/song?id=26491693&userid=421529315"

    #print(re.findall(r"\d+", str))
    id = int(re.findall(r"\d+", str)[1])
    start_urls = [
        "http://music.163.com/api/v1/resource/comments/R_SO_4_{}?limit=20&offset=0".format(id)
    ]
    # scrapy.Request(file_urls="https://v1.itooi.cn/netease/song?id={}".format(id))

    def parse(self,response):

        #print("\n\n",response['data']['count'],"\n\n")
        url="http://music.163.com/api/v1/resource/comments/R_SO_4_{0}?limit=20&offset={1}"

        webjson = json.loads(response.text)
        total = webjson["total"]
        for i in range(total//20+1):
            yield scrapy.Request(url=url.format(MySpider.id, i*20), callback=self.dataparse)
 

    def dataparse(self, response):
        items = quotes.items.MyItem()
        jsonlist = json.loads(response.text)
        comments = jsonlist["comments"]
        for content in comments:
            items['content'] = content["content"]
            yield items