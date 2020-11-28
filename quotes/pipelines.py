# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy
from PIL import Image
import requests
import numpy as np
import jieba
from wordcloud import WordCloud, ImageColorGenerator
#from scrapy.pipelines.files import FilesPipeline
class QuotesPipeline(object):
    def open_spider(self, spider):
        self.f = open("wywpl.txt","w",encoding='utf-8')

    def process_item(self, item, spider):

        #item = json.dumps(dict(item),ensure_ascii=False)
        print(item)

        text = item['content']
        print(text)
 #       input("断点")
        self.f.write(text+"\n")
        return item
#    def close_spider(self,spider, item):
    def close_spider(self,spider):
        input("关闭文件")
        self.f.close()
        input("开始词云图")
        text = open(r'wywpl.txt', "r", encoding="utf-8").read()
#        total = item['content']
        cut_text = jieba.cut(text)
        result = "/".join(cut_text)

        image = Image.open(r'书.png')
        graph = np.array(image)

        wc = WordCloud(font_path=r"shiguang.ttf", mask=graph, background_color='white', max_font_size=150)
        wc.generate(result)

        image_color = ImageColorGenerator(graph)
        wc.recolor(color_func=image_color)
        wc.to_file(r"wordcloud.png")
 #       newstr = "https://sc.ftqq.com/SCU52519Tc10bb3dc64eb724ee42ff4d1e26c4faf5cef536097212.send?text=成功爬取{}条评论。词云图制作完成了".format(total)

 #       print(newstr)
#        requests.get(newstr)

# class mp3FilesPipeline(FilesPipeline):
