# -*- coding:utf-8 -*-
import scrapy

class ToIp3366ProxyServerSpider(scrapy.Spider):
    name = 'ip3366'
    start_url ={
        'http://www.ip3366.net/free/'
    }
    def parse(self, response):
        for proxies in response.xpath('//*[@id="list"]'):
            yield {
                'IP': proxies.xpath('//*[@id="list"]/table/tbody/tr[1]/td[1]/text()').extract_first().strip(),
                'PORT':proxies.xpath('//*[@id="list"]/table/tbody/tr[1]/td[2]/text()').extract_first().strip(),
                'Anonymity':proxies.xpath('//*[@id="list"]/table/tbody/tr[1]/td[3]/text()').extract_first().strip(),
                'Mold':proxies.xpath('//*[@id="list"]/table/tbody/tr[1]/td[4]/text()').extract_first().strip(),
                'Location':proxies.xpath('//*[@id="list"]/table/tbody/tr[1]/td[5]/text()').extract_first().strip(),
                'Speed':proxies.xpath('//*[@id="list"]/table/tbody/tr[1]/td[6]/text()').extract_first().strip(),
                'LastTime': proxies.xpath('//*[@id="list"]/table/tbody/tr[1]/td[7]/text()').extract_first().strip(),
            }
            next_page_url=response.xpath('//*[@id="listnav"]/ul/a/@href').extract_first()