#WEBSCRAPPING
#We are looking at the english premier league table trying to get number of points for Arsenal
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import time
res = requests.get('https://www.premierleague.com/tables')
r = res.text #requests simply gets all tet along with html syntax
soup = BeautifulSoup(res.content, 'html.parser')  # beautiful soup gets only text and no html syntax
arsenal_points = soup.find_all('td', class_ = 'points')

print("Arsenal has ", arsenal_points[9].text, " points")
time.sleep(2)
#CORONAVIRUS DEATHS
deaths = requests.get('https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?%22%20%5Cl%22countries')
death = BeautifulSoup(deaths.content,'html.parser')
covid_deaths = death.find_all('div', class_='maincounter-number')
print("Number of Deaths worldwide are : ",covid_deaths[1].text)

