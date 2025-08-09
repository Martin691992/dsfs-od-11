import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
import os


class CrawlerLatLongHotels(scrapy.Spider):
    def __init__(self, name = 'Hotel2', **kwargs):
        super().__init__(name, **kwargs)
        

class RecupLatLong():
    def __init__(self):
        self.urls = []
        if not os.path.isfile('./data/hotels.csv') : 
            return
        # self.data = pd.read_csv('./data/hotels.csv')
        # print(self.data)
        with open('./data/hotels.csv', 'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                self.urls.append(line.split(',')[4])
                
            for a in self.urls:
                print(a)
                