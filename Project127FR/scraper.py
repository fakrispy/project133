from hashlib import new
import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import plotly.express

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("chromedriver_mac64/chromedriver")
browser.get(START_URL)

time.sleep(10)

scraped_data = []


def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    for row in table_rows:
        
        table_cols = row.find_all('td')
        temp_list = []

        print(table_cols)

        for col_data in table_cols:
            data = col_data.text.strip()
           ## print(data)
          ##  print(col_data.text)
            temp_list.append(data)
        scraped_data.append(temp_list)
    requests.get(START_URL)
    soup.find_all()
 

stars_data = []

for i in range(0, len(scraped_data)):
    star_names = scraped_data[i][1]
    distance = scraped_data[i][3]
    mass = scraped_data[i][5]
    radius = scraped_data[i][6]
    lum = scraped_data[i][7]
    required_data = [star_names, distance, mass, radius, lum]

    stars_data.append(required_data)
print(stars_data)
headers = ["Star_name", "Distance", "Mass", "Radius", "Luminocity"]
stars_def = pd.DataFrame(stars_data, columns = headers)
stars_def.to_csv("scraped_data.csv", index = True, index_label = "id")
stars_data.drop("NaN")
float = headers.astype({'Mass': 'float', 'Radius': 'float'})
solar_radius = radius.mul(0.102763)
solar_mass = mass.mul(0.000954588)

scraped_data.merge(new)
scraped_data.dropna()
scraped_data.axis = 1
scraped_data.describe()
scraped_data.info()
scraped_data.dtypes()

df = scraped_data.csv
scraped_data.download
scraped_data
radius_meters = solar_radius*6.957e+8
mass_kilo = solar_mass*1.989e+30
gravity_list = []
gravity = 6.67*(e-11)
list = []
solar_radius.append(list)
solar_mass.append(list)

fig = px.scatter(x = solar_radius, y=solar_mass)
fig.show()

            
    
    
scrape()