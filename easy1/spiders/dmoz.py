# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector

from easy1.items import DmozItem

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["http://www.rongshuxia.com/"]
    start_urls = [
        "http://www.rongshuxia.com/",
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="listCon"]/div[1]/div/ul[2]/li')
        items = []
        for site in sites:
            item = DmozItem()
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
#            desc = site.xpath('h3/text()').extract()
            desc = site.xpath('normalize-space(li[1]/h3/text())').extract()

            item['title'] = [t.encode('utf-8') for t in title]
            item['link'] = [l.encode('utf-8') for l in link]
            item['desc'] = [d.encode('utf-8') for d in desc]
            items.append(item)

        return items
