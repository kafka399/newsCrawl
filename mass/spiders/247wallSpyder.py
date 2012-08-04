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

class WallSpyder(CrawlSpider):
    name = '247wall'
    domain_name = "24wall"
    start_urls = ['http://247wallst.com/'+(datetime.strftime(datetime.now()-timedelta(1),'%Y'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%m'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%d'))]
    extra_domain_names = ["localhost"]
    

    rules = (
        Rule(SgmlLinkExtractor(allow='247wallst.com/'+(datetime.strftime(datetime.now()-timedelta(1),'%Y'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%m'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%d'))+"/",#page/\d'),
             restrict_xpaths='//a[@class="readmore"]'),
            'parse_item',
            follow=True,
        ),
             
        Rule(SgmlLinkExtractor(allow='247wallst.com/'+(datetime.strftime(datetime.now()-timedelta(1),'%Y'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%m'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%d'))+"/page/\d",
             restrict_xpaths='//div[@class="nav-previous"]'),
            'parse_page',
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
        item['date'] = datetime.strptime((hxs.select('//p[@class="post-meta"]//text()').extract())[0].split(': ')[1],'%B %d, %Y at %H:%M %p')#.strftime('%Y-%m-%d %H:%M')
        item['content']=(hxs.select('//div[@class="entry-content"]//p//text()').extract())
        item['title'] = (hxs.select('//h1[@class="entry-title"]//text()').extract())[0]
                                         
                       
        return item
