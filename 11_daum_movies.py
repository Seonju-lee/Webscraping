import requests
from bs4 import BeautifulSoup


#최근 5년
for year in range(2016,2021):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})


    for idx, image in enumerate(images):
        # print(image["src"]) #https로 시작하는거 있고 아닌거 있음
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1),"wb") as f:
            f.write(image_res.content) #파일로 만듦
        
        if idx >= 4: # 상위 5개 이미지까지만 다운로드
            break