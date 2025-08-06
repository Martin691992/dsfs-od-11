import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
import os


class HotelSpider(scrapy.Spider):
    name = 'hotels'
    def __init__(self, villes, resultats, ville_sans_hotels):
        self.villes = villes
        self.resultats = resultats
        self.ville_sans_hotels = ville_sans_hotels


    async def start(self):
        urls = self.villes
        for url in urls:
            request = scrapy.Request(
                url=url['url'],
                callback=self.parse,
                errback=self.parse_error,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0 Safari/537.36"}
            )
            request.cb_kwargs['ville'] = url['ville']
            request.cb_kwargs['id_ville'] = url['id_ville']
            request.cb_kwargs['url'] = url['url']
            yield request
        yield

    async def parse(self, response, ville, id_ville,url):
        titles = response.xpath('.//div[@data-testid="title"]/text()').getall()
        lien = response.xpath('//a[@data-testid="title-link"]/@href').getall()
        print(f"{id_ville}|{ville} : {titles[0] if len(titles) > 0 else "Pas d'hotel"} --- nombre d'hotels : {len(titles)}")
        retry_count = response.meta.get("retry_count", 0)
        if not titles and retry_count < 2:
            print(f"essai n°{retry_count}")
            yield response.request.replace(meta={"retry_count": retry_count + 1},dont_filter=True)

        if len(titles)>0:
            for a in titles:
                self.resultats.append({
                    "id_ville" : int(id_ville),
                    "ville":ville,
                    "url" : url,
                    "hotels" : a.replace(","," ")  ## il y a souvent des virgules dans les noms des hotels, donc on les squizzes
                })
        else :
            self.ville_sans_hotels.append({
                "id_ville" : int(id_ville),
                "ville":ville,
                "url" : url
            })
        


    def parse_error(self,failure):
        print(failure)
        yield


class Crawl(): 
    def __init__(self):
        self.anyVilles = False
        villes = []
        df = pd.read_csv('./data/wheather.csv')
        df_filtered = df[df['scrapp'] == 0]
        for i in df_filtered.values:
            villes.append({
                "id_ville" : int(i[0]),
                "ville":i[1],
                "url" : f"https://www.booking.com/searchresults.fr.html?ss={i[1]}"
                })
        if len(villes) == 0 :
            self.anyVilles = True
            return None
        premier_result, ville_no_hotels = self.lancerCrawler(villes=villes)
        id_in_results = [i.get('id_ville') for i in premier_result]
        df.loc[df["id"].isin(id_in_results) & (df["scrapp"] != 1), "scrapp"] = 1
        df.set_index('id',inplace=True)
        df.to_csv('./data/wheather.csv',encoding='utf-8')
        if os.path.isfile('./data/hotels.csv'):
            hotels = pd.read_csv('./data/hotels.csv')
            hotels.set_index('id_ville',inplace=True)
            new_hotels = pd.DataFrame(premier_result)
            new_hotels.set_index('id_ville',inplace=True)
            final = pd.concat([hotels,new_hotels])
            final.to_csv('./data/hotels.csv',encoding='utf-8')
        else:
            new_hotels = pd.DataFrame(premier_result)
            new_hotels.set_index('id_ville',inplace=True)
            new_hotels.to_csv('./data/hotels.csv',encoding='utf-8')
        
            
    def lancerCrawler(self, villes):
        resultats = []
        ville_sans_hotels = []
        spider = HotelSpider
        process = CrawlerProcess(settings={
            "FEEDS": {"resultats.json": {"format": "json"}},
            "LOG_LEVEL": "ERROR",
            "DOWNLOAD_DELAY": 1,
            # "RANDOMIZE_DOWNLOAD_DELAY": True,
        })
        process.crawl(spider,villes=villes,resultats=resultats,ville_sans_hotels=ville_sans_hotels)
        process.start()
        return resultats, ville_sans_hotels
