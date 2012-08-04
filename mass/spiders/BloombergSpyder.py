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

class BloombergAlpha(CrawlSpider):
    name = 'bloomberg'
    domain_name = "bloomberg"
    start_urls = ['http://www.bloomberg.com/archive/news/'+(datetime.strftime(datetime.now()-timedelta(1),'%Y'))+"-"+(datetime.strftime(datetime.now()-timedelta(1),'%m'))+"-"+(datetime.strftime(datetime.now()-timedelta(1),'%d'))]
    #start_urls = ['http://www.bloomberg.com/archive/news/2011-01-22/']
    extra_domain_names = ["localhost"]
    

    rules = (
        Rule(SgmlLinkExtractor(allow='http://www.bloomberg.com/news/2012-',deny='http://www.bloomberg.com/archive/news/2011',
             restrict_xpaths='//ul[@class="stories"]'),
            'parse_item',
            follow=True,
        ),
    )
    old_date = datetime.now()-timedelta(1)
    str_date=old_date.strftime('/%Y/%m/%d')
    
    def parse_page(self, response):
        print(response.url)
        
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = MassItem()
        
        
        item['guid'] = response.url
        item['date'] = datetime.strptime((hxs.select('//span[@class="datestamp"]//text()').extract()[1]),'%a %b %d %H:%M:%S GMT %Y')#.strftime('%Y-%m-%d %H:%M')
        item['content']=(hxs.select('//div[@id="story_content"]//p//text()').extract())
        c=""
        for b in item['content']:
            c = c + b.encode('utf-8').decode("unicode_escape").encode('ascii', 'ignore')
        
        item['content']= c 
        ln = item['content'].find("To contact the report")    
        if(ln>0):
            item['content']=item['content'][0:ln]
        
        ln = item['content'].find("To contact the author")    
        if(ln>0):
            item['content']=item['content'][0:ln]
        
        ln = item['content'].find("To contact the editor")
        if(ln>0):
            item['content']=item['content'][0:ln]
        
        ln = item['content'].find("To contact the Bloomberg")
        if(ln>0):
            item['content']=item['content'][0:ln]
        
        ln = item['content'].find("To contact the writter")
        if(ln>0):
            item['content']=item['content'][0:ln]
            
        ln = item['content'].find("To contact the author")
        if(ln>0):
            item['content']=item['content'][0:ln]    

        ln = item['content'].find("To contact the photo")
        if(ln>0):
            item['content']=item['content'][0:ln]    
            
            
            
                
        item['content'] = item['content'].replace("\n"," ")
        
        item['title'] = hxs.select('//h1[@class="disqus_title"]//text()').extract()
        
                                         
                       
        return item
