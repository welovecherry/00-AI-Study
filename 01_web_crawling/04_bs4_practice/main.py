# from bs4 import BeautifulSoup
# import requests

# # def get_html(url):
# #     """웹 페이지의 HTML을 가져오는 함수"""
# #     response = requests.get(url)
# #     return response.text

# # def parse_html(html):
# #     """HTML을 파싱하는 함수"""
# #     soup = BeautifulSoup(html, 'html.parser')
# #     return soup

# # def main():
# #     # 예제 URL (나중에 변경 가능)
# #     url = "https://example.com"
    
# #     # HTML 가져오기
# #     html = get_html(url)
    
# #     # HTML 파싱
# #     soup = parse_html(html)
    
# #     # 결과 출력
# #     print("페이지 제목:", soup.title.string)

# # if __name__ == "__main__":
# #     main()

# bsobj = BeautifulSoup("<html><body><h1>hihi</h1></body></html>")
# print(bsobj)

import requests
from bs4 import BeautifulSoup

# 예시 HTML 문자열 생성
html_example = """
<!DOCTYPE html>
<html>
<head>
    <title>Beautiful Soup 예제 페이지</title>
</head>
<body>
    <h1>Beautiful Soup 튜토리얼</h1>
    <div class="container">
        <p>Beautiful Soup은 HTML과 XML 파일에서 데이터를 추출하는 파이썬 라이브러리입니다.</p>
    </div>
    <div class="navigation">
        <a href="https://example.com/home">홈페이지</a>
        <a href="https://example.com/about">소개</a>
        <a href="https://example.com/contact">연락처</a>
    </div>
    <div class="result">첫 번째 결과</div>
    <div class="result">두 번째 결과</div>
    <h2>섹션 1</h2>
    <h3>서브섹션 1.1</h3>
</body>
</html>
"""

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_example, 'html.parser')

# 1. find() 메소드 예제
# print("===== find() 메소드 결과 =====")
# first_heading = soup.find('h1')
# print("첫 번째 h1 태그:", first_heading.text)

# link = soup.find('a', href="https://example.com/about")
# print("소개 링크:", link.text)

# element = soup.find('div', class_='container')
# print("container 클래스 내용:", element.text.strip())

# # 2. find_all() 메소드 예제
# print("\n===== find_all() 메소드 결과 =====")
# all_links = soup.find_all('a')
# print("모든 링크:")
# for i, link in enumerate(all_links, 1):
#     print(f"  {i}. {link.text}: {link.get('href')}")

# elements = soup.find_all(['h1', 'h2', 'h3'])
# print("\n모든 제목 태그:")
# for i, element in enumerate(elements, 1):
#     print(f"  {i}. {element.name}: {element.text}")
    
# results = soup.find_all('div', class_='result')
# print("\n모든 결과 클래스:")
# for i, result in enumerate(results, 1):
#     print(f"  {i}. {result.text}")

# # 3. 파일에서 파싱하기
print("\n===== 파일에서 파싱 결과 =====")

f = open("html_tag.html", encoding="utf-8")
bs_obj = BeautifulSoup(f.read(), "html.parser")
# print(bs_obj)
ul = bs_obj.find("ul")
# print(ul)
lis = ul.find_all("li")
# print(lis)

for li in lis:
    print(li.text)