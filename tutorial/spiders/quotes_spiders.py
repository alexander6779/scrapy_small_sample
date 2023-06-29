from pathlib import Path
import scrapy

# This is a small sample to see how scrapy works with the basics you can find  on the documentation.
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        """"
        For this example i wanna get the all html body from el-tiempo.net website
        """
        urls = [
            "https://www.el-tiempo.net/provincias/35",                
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Here I just choose the numer of the html file it returns me with the response.
        """
        page = response.url.split("/")[-1]
        filename = f"sample-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")