# -*- coding: utf-8 -*-

import logging
import scrapy
from wikiSpider.items import Article


class ArticleSpider(scrapy.Spider):
    logging.basicConfig(filename='example.txt', level=logging.DEBUG)
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_page", "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print "Title is " + title
        item['title'] = title
        return item