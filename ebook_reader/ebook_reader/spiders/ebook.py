from scrapy import Spider


class EbookSpider(Spider):
    name = 'ebook'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        print('[ PARSE ]')
        print(f'element "a" with title attribute generalized{response.css("a[title]").get()}')
        print(f'element "a" with href attribute{response.css("a[href]").get()}')
        print(f'element "a" with class attribute{response.css("a[class]").get()}')
        print(f'element "a" with title attribute specified{response.css("a[title = 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull']").get()}')
