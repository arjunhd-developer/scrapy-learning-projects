from scrapy import Spider


class EbookSpider(Spider):
    name = 'ebook'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        ebooks = response.css("article")
        print('[ PARSE ]')
        for ebook in ebooks:
            title = ebook.css('a::text').get()
            price = ebook.css('p.price_color::text').get()
            yield {
                "title": title,
                "price": price
            }



