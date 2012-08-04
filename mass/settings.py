# Scrapy settings for mass project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'mass'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['mass.spiders']
NEWSPIDER_MODULE = 'mass.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
  'mass.scrapymongodb.pipelines.MongoDBPipeline'
]

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'textmine'
MONGODB_COLLECTION = 'twentyseven'
MONGODB_UNIQ_KEY = 'guid'