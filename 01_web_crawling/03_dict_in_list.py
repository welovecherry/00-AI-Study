students = [
    {"이름": "김철수", "국어": 85, "수학": 90, "영어": 78},
    {"이름": "이영희", "국어": 92, "수학": 88, "영어": 95},
    {"이름": "박민수", "국어": 78, "수학": 95, "영어": 82}
]

# 방법 1: 특정 학생의 이름 출력
# print(students[0]["이름"])  # 첫 번째 학생의 이름 출력

# # 방법 2: 모든 학생의 이름 출력
# for student in students:
#     print(student["이름"])

# # # 방법 3: 리스트 컴프리헨션을 사용한 모든 이름 추출
# names = [student["이름"] for student in students]
# print(names)

# kim = students[0]
# print(kim)

''' shopping '''
cart = [
    {"상품명": "노트북", "가격": 1200000, "수량": 1},
    {"상품명": "마우스", "가격": 30000, "수량": 2},
    {"상품명": "키보드", "가격": 50000, "수량": 1}
]
# print(cart[0]["상품명"])
for item in cart:
    print(f"{item["상품명"]} - {item["가격"]}")

cart.append({"상품명": "new", "가격": 10, "수량":1})
print(cart)
