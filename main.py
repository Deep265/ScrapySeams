# Just a random file to text the program

from selenium.webdriver import Chrome

driver_path = 'C:/Users/Vrushali/Desktop/chromedriver.exe'

driver = Chrome(executable_path=driver_path)
driver.get('https://in.seamsfriendly.com/collections/shorts/products/sky-blue-crinkled-cotton-short-shorts')


xpath = '/html/body/div[7]/main/div[1]/section/div[1]/div[2]/div[1]/div/form/div[1]/variantswatchking/div/div/div/div/ul/li'
color_elements = driver.find_elements_by_xpath(xpath)

colors = []
for i in color_elements:
    print(i.get_attribute('orig-value'))
    colors.append(i.get_attribute('orig-value'))
print(colors)


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
    description.append(i.text)

print(len(text_info_elements),len(product_info_elements))



driver.quit()
