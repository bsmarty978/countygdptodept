import scrapy


class GdptodeptSpider(scrapy.Spider):
    name = 'gdptodept'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        data_set= response.xpath("//table/tbody/tr")
        for data in data_set:
            country = data.xpath(".//td[1]/a/text()").get()
            gdptodept = data.xpath(".//td[2]/text()").get()

            yield{
                'country': country ,
                'gdp_dept' : gdptodept
            }
