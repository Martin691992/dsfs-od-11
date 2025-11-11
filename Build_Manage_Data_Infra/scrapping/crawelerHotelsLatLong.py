import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
from etl_sql.data_base_connect.connection import Connector
import os


class CrawlerLatLongHotels(scrapy.Spider):
    def __init__(self, name = 'Hotel2', **kwargs):
        super().__init__(name, **kwargs)
        self.db = Connector()
        self.data = self.db.selectHotels()
        self.urls = [{"id" : a[0],"url":a[1]} for a in self.data]

    async def start(self):
        for url in self.urls:
            request = scrapy.Request(
                url=url['url'],
                callback=self.parse,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0 Safari/537.36"}
                )
            request.cb_kwargs['id_hotel'] = url['id']
            
            yield request
        yield

    async def parse(self, response,id_hotel):
        lat_lon  = response.xpath('//a[@id="map_trigger_header_pin"]/@data-atlas-latlng').get()
        retry_count = response.meta.get("retry_count", 0)
        if not lat_lon and retry_count < 2:
            print(f"essai n°{retry_count}")
            yield response.request.replace(meta={"retry_count": retry_count + 1},dont_filter=True)
        print(f"id de l'hotel : {id_hotel} - lat_long {lat_lon}")
        
        if(lat_lon):
            lat = lat_lon.split(",")[0] 
            lon = lat_lon.split(",")[1]
            try:
                self.db.updateLatLonHotels(lat,lon,id_hotel)
                print("Update ok")
            except:
                print("Erreur d'update")

class RecupLatLong():
    def __init__(self):
        self.lancerCrawler()
        return
    def lancerCrawler(self):
        spider = CrawlerLatLongHotels
        process = CrawlerProcess(settings={
            "LOG_LEVEL": "ERROR",
            "DOWNLOAD_DELAY": 0.5,
        })
        process.crawl(spider)
        process.start()

                