import scrapy
import time
from scrapy.utils.project import get_project_settings
from selenium.webdriver import Chrome, ChromeOptions
from ..items import SeamsItem

class ProductsSpider(scrapy.Spider):
    name = 'products'

    def start_requests(self):
        settings = get_project_settings()
        driver_path = settings.get('CHROME_DRIVER_PATH')
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(executable_path=driver_path,options=options)
        driver.get('https://in.seamsfriendly.com/collections/shorts')
        try:
            while True:
                button = driver.find_elements_by_xpath(
                    '//*[@id="shopify-section-collection-template"]/section/div[3]/div[2]/div[2]/div[4]/div/div[3]/div[2]/button')[
                    0]
                button.click()
                time.sleep(10)
        except:
            pass
        finally:
            xpath = "//div[@class='ProductItem__Wrapper']//a[text()]"
            link_elements = driver.find_elements_by_xpath(xpath)

        for link_el in link_elements:
            href = link_el.get_attribute("href")
            yield scrapy.Request(href)
        driver.quit()

    def parse(self, response):
        item = SeamsItem()
        item['title'] = response.xpath('normalize-space(//h1/text())').get()
        item['rating'] = response.css('span.jdgm-prev-badge__stars').attrib['data-score']
        item['images'] = list(response.xpath('//div[@class="Product__SlideshowNavScroller"]//img/@src').extract())
        item['price'] = response.xpath('//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div/span/text()').extract()[0]
        # selenium
        settings = get_project_settings()
        driver_path = settings.get('CHROME_DRIVER_PATH')
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(executable_path=driver_path, options=options)
        driver.get(str(response.request.url))
        xpath = '/html/body/div[7]/main/div[1]/section/div[1]/div[2]/div[1]/div/form/div[1]/variantswatchking/div/div/div/div/ul/li'
        color_elements = driver.find_elements_by_xpath(xpath)

        colors = []
        for i in color_elements:
            print(i.get_attribute('orig-value'))
            colors.append(i.get_attribute('orig-value'))
        product_info_path = '//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div[1]/div/div[7]/div[1]/ul/li'
        text_info_path = '//*[@id="shopify-section-product-template"]/section/div[1]/div[2]/div[1]/div/div[7]/div[1]/p'
        description = []
        product_info = []
        text_info_elements = driver.find_elements_by_xpath(text_info_path)
        product_info_elements = driver.find_elements_by_xpath(product_info_path)
        for i in text_info_elements:
            print(i.text)
            description.append(i.text)

        for i in product_info_elements:
            print(i.text)
            product_info.append(i.text)

        item['description'] = description
        item['product_info'] = product_info
        item['colors'] = colors
        yield  item

