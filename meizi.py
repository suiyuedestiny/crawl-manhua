import scrapy
from manhua.items import ManhuaItem

class MeiziSpider(scrapy.Spider):
    name = "meizi"
    allowed_domains = ["xieeqiao.com"]
    start_urls = ['http://www.xieeqiao.com/manhua/454_55.html']

    def parse(self, response):
        item = ManhuaItem()
        item['img_urls'] = response.xpath('/html/body/div[@class="main"]/div[1]/div[1]/div[2]/div[4]/a/img/@src').extract()
        yield item

        new_url_first = response.xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[10]/@href').extract_first()
        new_url = 'http://www.xieeqiao.com/manhua/' + new_url_first

        if new_url:
            yield scrapy.Request(new_url, callback=self.parse)
