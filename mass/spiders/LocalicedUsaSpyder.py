from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from datetime import datetime, date, time,timedelta
from scrapy.http import FormRequest, Request ,Headers
import re
from scrapy import log
from scrapy.utils.markup import remove_tags
from scrapy.selector import HtmlXPathSelector
import os, sys
cmd_folder = os.path.dirname(os.path.abspath(__file__))
print cmd_folder+'/items'
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
sys.path.insert(0, cmd_folder+'/items')
from mass.items import *

class LocalizedUsaSpyder(CrawlSpider):
    name = 'localizedusa'
    domain_name = "localizedusa"
    start_urls = ['http://localizedusa.com/'+(datetime.strftime(datetime.now()-timedelta(1),'%Y'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%m'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%d'))]
    extra_domain_names = ["localhost"]
    

    rules = (
        Rule(SgmlLinkExtractor(allow='http://localizedusa.com/',
            restrict_xpaths='//div[@class="navigation"]'),
            'parse_page',
            follow=True,
        ),
        
        Rule(SgmlLinkExtractor(allow='http://localizedusa.com/'+(datetime.strftime(datetime.now()-timedelta(1),'%Y'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%m'))+"/"+(datetime.strftime(datetime.now()-timedelta(1),'%d'))),
            'parse_item',
            follow=True,
        ),
             
        
    )
    
    
    
    def parse_page(self, response):
        print('done')
        
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = MassItem()
        item['guid'] = response.url
        item['title'] = hxs.select('//h1[@class="entry-title"]//text()').extract()
        item['date'] = datetime.strptime(re.sub(r"(st|nd|rd|th),", ",",(hxs.select('//p[@class="postmeta"]//text()').extract()[2].replace(' // ',''))),' on %b %d, %Y')#.strftime('%Y-%m-%d %H:%M')
        item['content']= hxs.select('//div[@class="entry"]//p//text()').extract()
           
        return item
