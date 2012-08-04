from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from datetime import datetime, date, time,timedelta
from scrapy.http import FormRequest, Request ,Headers
import re
from scrapy import log
from scrapy.selector import HtmlXPathSelector
import os, sys
cmd_folder = os.path.dirname(os.path.abspath(__file__))
print cmd_folder+'/items'
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
sys.path.insert(0, cmd_folder+'/items')
from mass.items import *

class SeekingAlpha(CrawlSpider):
    name = 'seekingalpha'
    domain_name = "seekingalpha"
    start_urls = ['http://seekingalpha.com/articles?page=3']
    extra_domain_names = ["localhost"]
    

    rules = (
        Rule(SgmlLinkExtractor(allow='http://seekingalpha.com',
             restrict_xpaths='//li[@class="previous"]'),
            'parse_page',
            follow=True,
        ),
             
        Rule(SgmlLinkExtractor(allow='http://seekingalpha.com/article/',
             restrict_xpaths='//ul[@class="stripes_list"]//div[@class="content"]'),
            'parse_item',
            follow=True,
        ),
    )
    old_date = datetime.now()-timedelta(1)
    str_date=old_date.strftime('/%Y/%m/%d')
    
    def parse_page(self, response):
        print('done')
        
    def parse_item(self, response):
       
        hxs = HtmlXPathSelector(response)
        item = MassItem()
        
        
        item['guid'] = response.url
        item['date'] = datetime.strptime((hxs.select('//div[@class="article_info_pos"]//text()').extract())[5],'%B %d, %Y')#.strftime('%Y-%m-%d %H:%M')
        item['content']=(hxs.select('//div[@id="article_body"]//text()').extract())
        item['title'] = hxs.select('//div[@id="page_header"]//h1//span//text()').extract()
        
                                         
                       
        return item
