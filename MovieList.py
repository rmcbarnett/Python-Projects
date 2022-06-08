from bs4 import BeautifulSoup
import requests
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage,"html.parser")
movies=soup.find_all(name ="h3", class_ ="title")
# print(movies)
movie_list = [f'{movie.get_text()}\n' for movie in movies]
movie_list.reverse()
print(movie_list)
with open('movies.txt', 'w') as fp:
    fp.writelines(movie_list)

