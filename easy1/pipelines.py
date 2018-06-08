# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import pymongo
import logging

from scrapy.conf import settings
from scrapy.exceptions import DropItem
#from scrapy import log

class DmozPipeline(object):
    def __init__(self):
#        self.file = codecs.open('dmoz_utf8.json', 'wb', encoding='utf-8')
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
#        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
#        self.file.write(line.decode("unicode_escape"))
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            logging.info("Booklist added to MongoDB database!")
#                    level=logging.DEBUG, spider=spider)
        return item

