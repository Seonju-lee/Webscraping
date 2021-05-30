import requests
res = requests.get("http://google.com") #정보를 가져오겠다
# print("응답코드:", res.status_code) # 200이면 정상 ->웹스크핑 가능

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")

res.raise_for_status() #문제가 생기면 오류 내뱉고 프로그램 끝내버림 (if문대신 사용가능)
# print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)
with open("mygoogle.html","w", encoding='utf-8') as f:
    f.write(res.text)