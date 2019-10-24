# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class InfomoneySpider(CrawlSpider):
    name = 'Infomoney'
    allowed_domains = ['infomoney.com.br']
    start_urls = ['https://infomoney.com.br/mercados/', 'https://infomoney.com.br/economia/' , 'https://infomoney.com.br/negocios/']

    rules = (
            Rule(
                LinkExtractor(
                    restrict_css=('a.cover-link')
                ), 
                callback='parse_new'
            ),
            Rule(
                LinkExtractor(
                    restrict_css=('span.hl-title-4  a')
                ), 
                callback='parse_new'
            ),
            Rule(
                LinkExtractor(
                    restrict_css=('span.hl-title-2  a')
                ), 
                callback='parse_new'
            )
        )

    def parse_new(self, response):
        title = response.css('.page-title-1::text').get()
        subtitle = response.css('.article-lead::text').get()
        author = response.css('.author-name a::text').get().strip()
        date = response.css('.posted-on time::attr(datetime)').get()

        text = " ".join(response.css('.article-content p ::text').getall())
        num_paragraph = len(response.css('.article-content p ::text'))
        subheadings = response.css('.article-content h2 strong::text').getall()

        num_links = len(response.xpath('//div[contains(@class, "article-content")]//p/a/@href | //div[contains(@class, "article-content")]//h2//a/@href'))       
        navigation_links = response.xpath('//div[contains(@class, "article-content")]//p/a[contains(@href, "mercados") or contains(@href,"economia") or contains(@href, "negocios")]/@href').getall()
        company_codes = response.xpath('//div[contains(@class, "article-content")]//h2//a[re:test(@href, "[a-zA-Z]{4}\d+")]/@href').re(r"[a-zA-Z]{4}\d")


        yield {
            'title': title,
            'subtitle': subtitle,
            'url': response.url,
            'author': author,
            'date': date,
            'text': text,
            'num_paragraph': num_paragraph,
            'subheadings': subheadings,
            'num_links': num_links,
            'company_codes': company_codes,
            'meta': response.meta
        }

        for page in navigation_links:
            yield scrapy.Request(
                response.urljoin(page),
                callback=self.parse_new
            )