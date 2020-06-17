# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BudgetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    release_date = scrapy.Field()
    movie_title = scrapy.Field()
    prod_budget = scrapy.Field()
    domestic_g = scrapy.Field()
    worldwide_g = scrapy.Field()

