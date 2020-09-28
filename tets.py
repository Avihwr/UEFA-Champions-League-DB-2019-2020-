## This is the main file which is used for scraping COVID-19 updates
import requests
from bs4 import BeautifulSoup
import re

# You can also get data for specific countries by changing the URL
# For example
# for US: https://www.worldometers.info/coronavirus/country/us/
# for India: https://www.worldometers.info/coronavirus/country/india/

url = "https://en.as.com/resultados/futbol/champions/2019_2020/ranking/jugadores/goles_favor/"
url1 = "https://www.eurosport.com/football/champions-league/2019-2020/standingperson.shtml"
url2 = "https://fontawesome.com/v4.7.0/cheatsheet/"
req = requests.get(url)
req1 = requests.get(url2)

# bsObj = BeautifulSoup(req.text, "html.parser")
# bs = BeautifulSoup(req.text, "html.parser")
bs1 = BeautifulSoup(req.text, "html.parser")
# bsO = BeautifulSoup(req1.text, "html.parser")

# Name = bsObj.find_all("span", class_="name")
# Goals = bs.find_all("td", attrs={'class': 'cantidad'})
# Team = bsO.find_all("div", class_="col-md-4 col-sm-6 col-lg-3 col-print-4")
image = bs1.find_all("img")

r = image[10:]


for i in r:
    w = '(' "'" + str(i) + "'" + "," + "'" + str(i) + "'" ')' + ','
    print(str(w))




# lst1 = []
# for n in range(0, 50):
#     n = Team[n].text.strip()
#     lst1.append(n)
# print(lst1)
#
# lst = []
# for i in range(0, 50):
#     y = Name[i].text.strip()
#     lst.append(y)
# # print(lst)
#
# o = str(Goals)
# x = re.findall('''\d+''', o)
# for k, p in zip(x, lst):
#     # for i in range(0, 100):
#     t = '(' + "'" + p + "'" + "," + k + ')' + ','
#     print(t)

# print(x)


# ('Lewandowski',32,98)
# ,('Erling Braut Haaland',20, 88)
# ('Serge Gnabry',25,90),
# ('Rahim Sterling',25,92),
# ('Memphis Depay',26,89),
# ('Harry Kane',27,91),
# ('Dries Mertens',33,92),
# ('Gabriel Jesus',23,90),
# ('Josip Ilicic',32,87),
# ('Kylian Mbappe',21,95),
# ('Icardi',27,93),
# ('Karim Benzema',32,90),
# ('Luis Suárez',33,96),
# ('Heung-Min Son',28,90),
# ('Lautaro Martínez',23,89),
# ('Rodrygo',19,86),
# ('Mislav Orsic',27,84),
# ('Mohamed Salah',28,91),
# ('Emil Forsberg',28,87),
# ('Thomas Müller',30,93),
# ('Cristiano Ronaldo',35,96),
# ('M. Sabitzer',26,84),
# ('Timo Werner',24,89),
# ('Achraf Hakimi',21,88),
# ('Quincy Promes',28,89),
# ('Pasalic',25,83),
# ('Tammy Abraham',22,82),
# ('Angel Di María',32,89),
# ('Neymar Jr.',28,97),
# ('Arkadiusz Milik',26,91),
# ('Paulo Dybala',26,90),
# ('Dani Olmo',22,85),
# ('Oxlade-Chamberlain',27,87),
# ('Tolisso',26,89),
# ('Perisic',31,91),
# ('João Félix',20,89),
# ('Hwang Hee-Chan',24,84),
# ('Pizzi',30,83),
# ('Coutinho',28,88),
# ('Kingsley Coman',24,89),
# ('Lionel Messi',33,99),
# ('Álvaro Morata',27,91),
# ('Mbwana Aly Samatta',27,80),
# ('El-Arabi',33,84),
# ('Nelson Semedo',26,88),
# ('Tomas Soucek',25,78),
# ('Higuaín',32,86),
# ('Joshua Kimmich',25,92),
# ('Takumi Minamino',25,87),
# ('Sergio Ramos',34,97);
