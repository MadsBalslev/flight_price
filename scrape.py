from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep

webdriver = "./chromedriver"

options = Options()
options.headless = True

args = ["window-size=1400,2100"]

def get_price():
    driver = Chrome(webdriver, options=options, service_args=args)
    driver.get(url)

    # sleep(2)

    price = driver.find_element_by_class_name('gws-flights-results__cheapest-price')
    print(price.text)

    driver.close()

org = input("Where are you flying from?\n (IATA Code) -> ").upper()
dest = input("Where are you flying to? \n (IATA Code) -> ").upper()
round_trip = input("Are you doing a round trip? (Y/n) \n -> ")
px = input("How many people are traveling? \n -> ")
dep_date = input("When are you flying out? (YYYY-MM-DD) \n -> ")

url = f"https://www.google.com/flights?hl=da#flt={org}.{dest}.{dep_date};tt:o;px:{px}"

if round_trip.lower() == "y":
    ret_date = input("When are you heading home? (YYYY-MM-DD) \n -> ")
    url = f"https://www.google.com/flights?hl=da#flt={org}.{dest}.{dep_date}*{dest}.{org}.{ret_date};px:{px}"


# print(url)
get_price()

