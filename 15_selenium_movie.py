import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    } #get users agent string #한글 언어로 된 페이지 반환
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies)) 
#동적페이지라 로딩되기 전 10개 영화만 반환함. -> 전체 보기위해 셀레니움 사용할 것임

# with open("movie.html", "w", encoding="utf8") as f:  #파일로 만들기 "w" -> 쓰기 모드
#     # f.write(res.text)
#     f.write(soup.prettify()) #html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)