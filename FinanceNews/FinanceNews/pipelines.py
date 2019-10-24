# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.exceptions import DropItem
import logging

class FinancenewsPipeline(object):
    
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            db_uri = settings.get('MONGO_URI'),
            db_database = settings.get('MONGO_DATABASE'),
            db_collection = settings.get('MONGODB_COLLECTION')
        )

    def __init__(self, db_uri, db_database, db_collection):
        self.ids_seen = set()
        self.db_uri = db_uri
        self.db_database = db_database
        self.db_collection = db_collection

    def open_spider(self, spider):
        ## opening db connection
        self.client = pymongo.MongoClient(self.db_uri)
        self.db = self.client[self.db_database]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        if item['url'] in self.ids_seen:
            logging.debug("Duplicate item found on crawling: %s" % item)
            raise DropItem("Duplicate item found on crawling: %s" % item)
        else:
            self.ids_seen.add(item['url'])    
            if self.db[self.db_collection].find({'url': dict(item)['url']}).limit(1).count() > 0:
                logging.debug("Duplicate item found on DB: %s" % item)
                raise DropItem("Duplicate item found on DB: %s" % item)
            else:
                logging.debug("Post added to MongoDB")
                self.db[self.db_collection].insert(dict(item))
            
            return item