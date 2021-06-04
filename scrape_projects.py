import scrapy
from bs4 import BeautifulSoup


NEXT_PAGE_SELECTOR = "#block-mainpagecontent > div > div > nav > ul > li.pager__item.pager__item--next > a"
ITEM_URL_SELECTOR = ".field.field--name-title.field--type-string.field--label-above > a"


def get_text_from_html(html_str):
    return BeautifulSoup(html_str).get_text()


class BlogSpider(scrapy.Spider):
    name = "blogspider"
    start_urls = ["https://navigator.innovation.ca/en/search"]

    def parse(self, response):
        for item in response.css(ITEM_URL_SELECTOR):
            yield response.follow(item, self.parse_item)

        # for next_page in response.css(NEXT_PAGE_SELECTOR):
        #     yield response.follow(next_page, self.parse)

    def parse_item(self, response):
        research_service_items = ",\n".join(
            [
                item.get()
                for item in response.css(
                    "#block-mainpagecontent > article > div > div.clearfix.text-formatted.field.field--name-field-research-services.field--type-text-long.field--label-above > div.field__item"
                ).xpath("ul/li/text()")
            ]
        )

        yield {
            "project_title": response.css("#block-pagetitle > h1 > span::text").get(),
            "institution": response.css(
                "#block-views-block-facility-block-facility-address > div > div > div > div > div > span::text"
            ).get(),
            "what_the_facility_does": get_text_from_html(
                response.css(
                    "#block-mainpagecontent > article > div > div.clearfix.text-formatted.field.field--name-field-what-the-lab-facility-does.field--type-text-long.field--label-above > div.field__item"
                ).get()
            ),
            "research_services": research_service_items,
        }
