# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FinancenewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
    num_paragraph = scrapy.Field()
    subheadings = scrapy.Field()
    num_links = scrapy.Field()
    company_codes = scrapy.Field()
    meta = scrapy.Field()
    collect_date = scrapy.Field
