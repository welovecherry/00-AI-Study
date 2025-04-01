import requests

#     # what is the url rule like '&display= &start"'??
    # url =  "https://openapi.naver.com/v1/search/blog.json?query=교대역 맛집&display=200"






class Naver_Search_api():
    api_url = "https://openapi.naver.com/v1/search/blog.json"

    def call_api(self, keyword, start=1, display=10): 
        url =  f"{self.api_url}?query={keyword}&start={start}&display={display}"
        res = requests.get(url, headers={"X-Naver-Client-Id": "VZR2mJ_YLeP1bVIJtoNj", 
                                        "X-Naver-Client-Secret":"xKLX7y5huF"})
        r = res.json()
        return r

    def get_paging_call(self, keyword, quantity):
        if quantity > 1100:
            exit("최대 요청할 수 있는 건수는 1100건입니다")
        repeat = quantity // 100 # 100으로 나눈 몫
        result = []
        display = 100
        if quantity < 100:
            display = quantity
            repeat = 1

        for i in range(repeat):
            start = (i * 100) + 1
            if start > 1000:
                start = 1000
            print(f"{i+1}번 반복합니다. start:{start}")
            r = self.call_api(keyword, start=start, display=display)
            result += r["items"]
        return result
    def blog(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        return self.get_paging_call(keyword, quantity)
    def news(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.get_paging_call(keyword, quantity)



if __name__ == '__main__':
    naver_search_api = Naver_Search_api()
    r = naver_search_api.blog("수서역 맛집", 100)
    # print(r)
    print(r[0])
    print(len(r))

    # if isinstance(r, list) and len(r) > 0:
    #     for item in r:
    #         if "items" in item and isinstance(item["items"], list) and len(item["items"]) > 0:
    #             print(item["items"][0])
    #         else:
    #             print("No items found or 'items' is not a list.")
