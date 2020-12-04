# Visit https://forecast.weather.gov/
# pip install beautifulsoup4
# pip install requests
# pip install Pandas3

import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1",
           "DNT": "1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.X8hl180za00', headers=headers, timeout=5, allow_redirects=True)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup) # prints whole html code of that page
# print(soup.find_all('a'))  # prints all 'a' tags in that page

week = soup.find(id='seven-day-forecast-body')
# print(week)  # prints whole 'div' with 'seven-day-forecast-body' as id
items = week.find_all(class_='tombstone-container')
# print(items)  # prints whole 'div' with 'tombstone-container' as class
# print(items[1])

# print(items[1].find(class_="period-name").get_text())
# print(items[1].find(class_="short-desc").get_text())
# print(items[1].find(class_="temp").get_text())

period_names = [item.find(class_="period-name").get_text()
                for item in items[1:]]
short_descriptions = [
    item.find(class_="short-desc").get_text() for item in items[1:]]
temperatures = [item.find(class_="temp").get_text() for item in items[1:]]
""" print(period_names)
print(short_descriptions)
print(temperatures) """

weather_stuff = pd.DataFrame({
    "period": period_names,
    "short_descriptions": short_descriptions,
    "temperatures": temperatures,
})

print(weather_stuff)  # Pandas helps in printing this data in table format

weather_stuff.to_csv('weather.csv')  # saves the file in .csv format
