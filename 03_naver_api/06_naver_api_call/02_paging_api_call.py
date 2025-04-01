import requests

    # what is the url rule like '&display= &start"'??
    # url =  "https://openapi.naver.com/v1/search/blog.json?query=교대역 맛집&display=200"
def call_api(keyword, start, display): 
    url =  f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url, headers={"X-Naver-Client-Id": "VZR2mJ_YLeP1bVIJtoNj", 
                                    "X-Naver-Client-Secret":"xKLX7y5huF"})
    # print(res.text)
    # print(res.json())
    r = res.json()
    # for item in r["items"]:
    #     print(item)
    return r


def get_paging_call(keyword, quantity):
    repeat = 9
    for i in range(repeat):
        print(f"{i+1}번 반복합니다")




# what is 'if __name__ == '__main__' ??
# 페이징?
if __name__ == '__main__':
    # 100건 넘게 작업하려면 페이징 해야한다. 최대 호출 갯수: 1100건
    # r = call_api("수서 맛집", 1000, 100)
    # r = call_api("수서 맛집", 101, 100)
    # r = call_api("수서 맛집", 201, 100)
    # r = call_api("수서 맛집", 301, 100)
    # for item in r["items"]:
    #     print(item)

    r = get_paging_call("수서 맛집", 900)
