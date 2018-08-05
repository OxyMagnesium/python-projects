
print("")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import html
import time

chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
driver_path = r'E:\Python\chromedriver.exe'

tierlist = {1 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=396,420', #GT 1030/RX 550
            2 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=379,395', #GTX 1050/RX 560
            3 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=380', #GTX 1050 Ti
            4 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=378,392', #GTX 1060 3GB/RX 570
            5 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=373,391', #GTX 1060 6GB/RX 580
            6 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=369', #GTX 1070
            7 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=415,404', #GTX 1070 Ti/RX VEGA 56
            8 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=367,405', #GTX 1080/RX VEGA 64
            9 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=390'} #GTX 1080 Ti

print(
'''
GPU tierlist:
1: GT 1030/RX 550
2: GTX 1050/RX 560
3: GTX 1050 Ti
4: GTX 1060 3GB/RX 570
5: GTX 1060 6GB/RX 580
6: GTX 1070
7: GTX 1070 Ti/RX VEGA 56
8: GTX 1080/RX VEGA 64
9: GTX 1080 Ti
'''
)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = chrome_path

tier = input("Enter GPU tier to find: ")

if str(tier) not in str(tierlist.keys()):
    print("\n" + "ERROR: Invalid GPU tier")
    end_stop = input("Press enter to quit.")
    quit()

for tiern in tierlist:
    if str(tiern) == str(tier):
        tier = tierlist[tiern]
        break

print("")

print("Connecting...")

driver = webdriver.Chrome(executable_path = driver_path, chrome_options = chrome_options)
driver.get(tier)

print("")

print("Processing...")

name = ""
price = ""
link = ""

while str(*name) == "" and str(*link) == "" and str(*price) == "":
    page = driver.page_source
    tree = html.fromstring(page)
    name = tree.xpath('(//td[@class="tdname"]/a/text())[1]')
    price = tree.xpath('(//td[@class="tdprice"]/text())[1]')
    link = tree.xpath('(//td[@class="tdname"]/a/@href)[1]')

driver.quit()

print("")

print("Found recommended GPU:")
print(str(*name) + " - " + str(*price))
print("https://pcpartpicker.com" + str(*link))

print("")

end_stop = input("Press enter to quit.")
