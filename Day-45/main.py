import requests
from bs4 import BeautifulSoup
import requests
# import lxml
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response= requests.get(URL)
arc_webpage = response.text

soup= BeautifulSoup(arc_webpage,"html.parser")

all_names= soup.find_all(name="h3",class_="title")
moviesList= []
for name in all_names:
    # temp_names= " ".join(name.getText().split()[1:4])
    moviesList.append(name.getText())

moviesList.reverse()

for i in moviesList:
    print(i)


with open("moviesList.txt","w",encoding="utf-8") as file:
    for item in moviesList:
        file.write(f"str({item}) \n")