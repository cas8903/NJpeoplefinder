import scrapy


class spider(scrapy.Spider):
    name = "spiderI"
    allowed_domains = ["https://answers.yahoo.com"]

    initialURL = [
        "https://answers.yahoo.com/dir/index?sid=396545443"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)