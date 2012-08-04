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

class BarronTechBlogSpyder(CrawlSpider):
    name = 'barrontechblog'
    domain_name = "barrontechblog"
    start_urls = ['http://blogs.barrons.com/techtraderdaily/page/3/']
    extra_domain_names = ["localhost"]
    

    rules = (
        Rule(SgmlLinkExtractor(allow='http://blogs.barrons.com/techtraderdaily',
            restrict_xpaths='//li[@class="blognav_next"]'),
            'parse_item',
            follow=True,
        ),
    )
    
    old_date = datetime.now()-timedelta(1)
    str_date=old_date.strftime('/%Y/%m/%d')
    counter=0
    
    def parse_page(self, response):
        print('done')
        
    def parse_item(self, response):
        
        hxs = HtmlXPathSelector(response)
        guid = hxs.select('//div[@class="postContent"]//h2//a//@href').extract()
        title = hxs.select('//div[@class="postContent"]//h2//a//text()').extract()
        content = hxs.select('//div[@class="postContent"]').extract()
        date = hxs.select('//small[@class="timeStamp"]').extract()
        counter=0
        items = []
        for it in guid:                                 
            item = MassItem()
            item['guid'] = it
            item['date'] = datetime.strptime(re.sub('^\n[ ]+','',re.sub('[ ]+$','',remove_tags((date[counter])))), '%b %d, %Y%H:%M %p')#.strftime('%Y-%m-%d %H:%M')
            item['content']= remove_tags(content[counter])
            item['content'] = item['content'].replace("\n"," ")
            item['title'] = title[counter]
            counter=counter+1
            items.append(item)   
        return items
