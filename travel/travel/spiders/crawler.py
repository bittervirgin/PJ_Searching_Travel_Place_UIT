# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
import os

class TopTenPost(scrapy.Spider):
    name = "travel"
    allowed_domain = "toptentravel.com.vn"
    start_urls = [
        "https://toptentravel.com.vn/tour-du-lich-da-lat-3n2d.html"
        ]
        

#title and price    
    def parse(self,response):
    #output = open('topten_Des.txt','w')
    #resp = Selector(response)  
    #response = HtmlResponse(url=url, body=body)
        #tags = response.xpath('//div[@id="wrap"]').getall()
        #for path in tags:
            #desc = path.xpath('//div[@class="__single_des"]/text()').get()
            #for div in path.xpath('//div[@class="col-md-9.__ctn_right"]').getall():
        container = response.xpath('//section[@class="container"]')
        for content in container:
            top_content = container.xpath('//section[@id="__single_top_content"]/div[@class="col-md-6 __single_tour_description"]')
            des = top_content.xpath('//p[@class="__single_des"]/text()').get()
            bottom_content = container.xpath('//section[@id="__single_bottom_content"]')
            #inf = bottom_content.xpath('//div[@class="tabcontent_chuongtrinh"]')
            #lichtrinh = inf.xpath('//p/text()').getall()
        #desc = response.xpath('//p[@class="__single_des"]/text()').get()
        title = response.css('title::text').get()
        filename = os.path.join(r'C:\Users\yaiba\UIT\Inform_Retreive\PJ_Searching_Travel_Place_UIT\Data',"%s.txt" %title)
        with open(filename,"w",encoding="UTF-8") as f:
            f.write(des)
            #f.writelines(inf)
        self.log('Saved file %s' %filename)

