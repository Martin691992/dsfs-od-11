import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
import os


class CrawlerLatLongHotels(scrapy.Spider):
    def __init__(self, name = 'Hotel2', **kwargs):
        super().__init__(name, **kwargs)
        self.urls = []
        if not os.path.isfile('./data/hotels.csv') : 
            return
        with open('./data/hotels.csv', 'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                self.urls.append(line.split(',')[4])
        self.urls = self.urls[1:]

    async def start(self):
        for url in self.urls:
            request = scrapy.Request(
                url=url,
                callback=self.parse,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0 Safari/537.36"}
                )
            yield request
        yield

    async def parse(self, response):
        lat_lon  = response.xpath('//a[@id="map_trigger_header_pin"]/@data-atlas-latlng').get()
        print(lat_lon)

class RecupLatLong():
    def __init__(self):
        self.lancerCrawler()
        return
    def lancerCrawler(self):
        spider = CrawlerLatLongHotels
        process = CrawlerProcess(settings={
            "LOG_LEVEL": "ERROR",
            "DOWNLOAD_DELAY": 1,
        })
        process.crawl(spider)
        process.start()

                