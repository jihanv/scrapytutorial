import scrapy

# venv\Scripts\Activate.ps1
# deactivate

# scrapy crawl bookspider

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # to get all the books
        books = response.css('article.product_pod')

        #Iterate through the books to get information
        for book in books:
            yield{
                'name': book.css('h3 a::text').get(),
                'price': book.css('.product_price .price_color::text').get(),
                'url': books.css('h3 a').attrib['href']
            }