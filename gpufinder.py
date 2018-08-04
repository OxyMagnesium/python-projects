
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import html
import time

print("")

print("Initializing...")

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

print("Connecting...")

driver = webdriver.Chrome(executable_path = r'E:\Python\chromedriver.exe', chrome_options = chrome_options)
driver.get('https://pcpartpicker.com/products/video-card/#sort=price&c=373,391')

print("")

print("Processing...")

name = ""
link = ""

while str(*name) == "" and str(*link) == "":
    page = driver.page_source
    tree = html.fromstring(page)
    name = tree.xpath('(//td[@class="tdname"]/a/text())[1]')
    link = tree.xpath('(//td[@class="tdname"]/a/@href)[1]')

driver.quit()

print("")

print("Found recommended GPU.")
print("Name: " + str(*name))
print("PCPP link: https://pcpartpicker.com" + str(*link))

print("")

end_stop = input("Press enter to quit.")
