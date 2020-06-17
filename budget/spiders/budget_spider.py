from budget.items import BudgetItem
from scrapy import Spider


class BudgetSpider(Spider):
    name = 'budget_spider'
    allowed_urls = ['https://www.the-numbers.com/']
    start_urls = ['https://www.the-numbers.com/movie/budgets/all']

    def parse(self, response):
        rows = response.xpath(
            '//*[@id="page_filling_chart"]/center/table//tr')[1:]

        for row in rows:
            rank = int(row.xpath('./td[1]/text()').extract_first())
            release_date = row.xpath('./td[2]/a/text()').extract_first()
            movie_title = row.xpath('./td[3]//text()').extract_first()
            prod_budget = row.xpath('./td[4]/text()').extract_first().strip()
            domestic_g = row.xpath('./td[5]/text()').extract_first().strip()
            worldwide_g = row.xpath('./td[6]/text()').extract_first().strip()

        item = BudgetItem()
        item['rank'] = rank
        item['release_date'] = release_date
        item['movie_title'] = movie_title
        item['prod_budget'] = prod_budget
        item['domestic_g'] = domestic_g
        item['worldwide_g'] = worldwide_g
        yield item
