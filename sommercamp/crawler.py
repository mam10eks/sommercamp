from resiliparse.extract.html2text import extract_plain_text
from scrapy import Spider, Request
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http.response.html import HtmlResponse


class SchoolSpider(Spider):
    name = "tea"

    start_urls = [
        "https://de.wikipedia.org/wiki/Autismus",
        "https://en.wikipedia.org/wiki/Autism",
        "https://simple.wikipedia.org/wiki/Autism",
        "https://www.autismus.de",
        "https://www.autismus.org",]
    link_extractor = LxmlLinkExtractor(
        allow_domains=["de.wikipedia.org", 
                       "en.wikipedia.org", 
                       "simple.wikipedia.org",
                       "www.autismus.de",
                       "www.autismus.org"]
    )
 
    custom_settings = {
        "USER_AGENT": "Sommercamp (yuchaofen03@gmail.com)",
        "ROBOTSTXT_OBEY": True,
        "CONCURRENT_REQUESTS": 4,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 1,
        "HTTPCACHE_ENABLED": True,
    }

    def parse(self, response):
        if not isinstance(response, HtmlResponse):
            return
        
        yield {
            "docno": str(hash(response.url)),
            "url": response.url,
            "title": response.css("title::text").get(),
            "text": extract_plain_text(response.text, main_content=True),
        }

        for link in self.link_extractor.extract_links(response):
            if link.text == "":
                continue
            yield Request(link.url, callback=self.parse)