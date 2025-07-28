import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess


class HotelSpider(scrapy.Spider):
    name = 'hotels'
    async def start(self):
        urls = []
        df = pd.read_csv('./Build_and_Manage_a_Data_Infrastructure/data/wheather.csv')
        for i in df['name']:
            urls.append(f"https://www.booking.com/searchresults.fr.html?ss={i}")
        
        for url in urls:
            print(url)
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0 Safari/537.36"}
            )

    async def parse(self, response):
        titles = response.xpath('//div[@data-testid="property-card"]//div[@data-testid="title"]/text()').getall()
        print(titles[0])
        yield

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {"resultats.json": {"format": "json"}},
        "LOG_LEVEL": "ERROR",
    })
    process.crawl(HotelSpider)
    process.start()

#"https://www.booking.com/searchresults.fr.html?ss=Lyon&label=fr-fr-booking-desktop-DCpBIW3k2*WIo8XuzMdB9AS652796013276%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9056017%3Ali%3Adec%3Adm&aid=2311236&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1448468&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=d5b268f6380902e9&ac_meta=GhBkNWIyNjhmNjM4MDkwMmU5IAAoATICZnI6BGx5b25AAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0"
# request = "https://www.booking.com/searchresults.fr.html?ss=Lyon"



# //*[@id="main"]/div/div/div/div/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div[1]/div/div[1]/div/h3