
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import html
import time

chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
driver_path = r'E:\Python\chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = chrome_path

#-------------------------------------------------------------------------------

CPU = {
       'xpulink' : {

                   }
       ,
       'xpulist' : '''

                   '''
      }

GPU = {
       'xpulink' : {
                    1 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=396,420', #GT 1030/RX 550
                    2 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=379,395', #GTX 1050/RX 560
                    3 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=380', #GTX 1050 Ti
                    4 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=378,392', #GTX 1060 3GB/RX 570
                    5 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=373,391', #GTX 1060 6GB/RX 580
                    6 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=369', #GTX 1070
                    7 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=415,404', #GTX 1070 Ti/RX VEGA 56
                    8 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=367,405', #GTX 1080/RX VEGA 64
                    9 : 'https://pcpartpicker.com/products/video-card/#sort=price&c=390' #GTX 1080 Ti
                   }
       ,
       'xputext' : '''
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
      }

#-------------------------------------------------------------------------------

def get_partlist():
    while True:
        intake = input("Enter part category (CPU/GPU): ").lower()
        if intake == 'cpu':
            return CPU
        if intake == 'gpu':
            return GPU

        print("ERROR: Invalid input. Try again.\n")


def get_partlink():
    print(partlist['xputext'])

    while True:
        part = input("Enter part tier: ")
        for tier in partlist['xpulink']:
            if str(tier) == str(part):
                return str((partlist['xpulink'])[tier])

        print("ERROR: Invalid input. Try again.\n")


def retrieve_data(partlink):
    print("Connecting...")

    driver = webdriver.Chrome(executable_path = driver_path, chrome_options = chrome_options)
    driver.get(partlink)

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

    return {'name': name, 'price': price, 'link': link}

    driver.quit()

#-------------------------------------------------------------------------------

print("Welcome to partfinder v0.1")

print("")

print("What would you like to search for?")
partlist = get_partlist()

print("")

print("What parts are you looking for?")
partlink = get_partlink()

print("")

data = retrieve_data(partlink)

print("")

print("Found recommended part:")
print(str(*data['name']) + " - " + str(*data['price']))
print("https://pcpartpicker.com" + str(*data['link']))

print("")

end_stop = input("Press enter to quit.")
quit()
