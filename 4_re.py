import re
#abcd, book, desk
#ca?e

p = re.compile("ca.e") 
# . : 하나의 문자를 의미
# ^ : 문자열의 시작 (^뒤의 문자열로 시작하는 것)
# & : 문자열의 끝 (이걸로 끝나라)

def print_match(m):
    if m :
        print("m.group():",m.group() ) # 일치하는 문자열 반환
        print("m.string:", m.string) #입력받은 문자열
        print("m.start():", m.start()) #일치하는 문자열의 시작 index
        print("m.end():", m.end()) #일치하는 문자열의 끝 index
        print("m.span():", m.span()) #일치하는 문자열의 시작/끝 index
    else:
        print("매칭되지 않음")

# m =p.match("careless") #주어진 문자열의 처음부터 매칭되는지 확인(뒷부분 확인안하고 넘어감)
# print_match(m)
# print(m.group()) #매치되지 않으면 에러가 발생

m =p.search("good care") #serach: 주어진 문자열중에 일치하는게 있는지
print_match(m)

lst = p.findall("good care cafe") #findall :일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 1. re.compile("원하는 형태")
#2. m = p.match("비교할 문자열")
#3. m = p.search("비교할 문자열")
#4. lst = p.findall("비교할 문자열")

#원하는 형태 : 정규식