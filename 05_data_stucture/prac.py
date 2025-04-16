# lst = [1, 2, 3]

# x = lst.pop()
# # print(x)
# # print(lst)

# words = ['a', 'b', 'c']
# res = '-'.join(words)
# print(res)

# from collections import deque

# dq = deque([1, 2, 3])

# dq.append(4)
# dq.appendleft(0)
# dq.pop()
# dq.popleft()
# print(dq)


# from collections import Counter

# cnt = Counter('banana')
# # print(cnt['a'])
# print(cnt.most_common(1))


# from collections import defaultdict

# dd = defaultdict(int)
# # print(dd)
# dd['a'] = 11;
# print(dd)

# lst = [5, 4, 3, 2, 1]
# lst.sort(reverse=True)
# print(lst)

# # new_lst = sorted(lst)
# # print(new_lst)

# my_list = [5, 1, 4, 2, 3]
# # my_list.sort(reverse=True)
# new_list = sorted(my_list)
# print(my_list, new_list)

# my_tuple = (5, 1, 4, 2, 3)
# print(f"원본 튜플: {my_tuple}")

# sorted_list = sorted(my_tuple)
# print(sorted_list)

# my_string = "Python"
# print(f"\n원본 문자열: {my_string}")

# sorted = sorted(my_string, reverse=True)
# print(my_string, sorted)

# words = ["banana", "apple", "kiwi", "strawberry", "orange"]

# sorted = sorted(words, key=len, reverse=True)
# print(sorted)

# mixed_case_words = ["Banana", "apple", "Cherry", "date"]
# sorted_w = sorted(mixed_case_words, key=str.lower)
# print(sorted_w)

# students = [('Alice', 90), ('Bob', 85), ('Charlie', 95)]
# sorted_s = sorted(students, key=lambda x: x[1], reverse=True)
# print(sorted_s)
# from collections import defaultdict

# adj_list = defaultdict(list)
# edges = [(1, 2), (1, 0), (1, 3), (0, 3), (2, 3), (3, 4)]

# for u, v in edges:
#     adj_list[u].append(v)
#     adj_list[v].append(u)

# # for node in sorted(adj_list.keys()):
# #     print(sorted(adj_list[node]))
# # for node in sorted(adj_list.keys()):
# #     print(f"정점 {node}의 이웃: {sorted(adj_list[node])}")
# node_to_check = 4
# print(sorted(adj_list[node_to_check]))

# from collections import defaultdict

# graph_prac = defaultdict(list)
# directed_edges = [('A', 'B'), ('B', 'C'), ('B', 'E'), ('E', 'D'), ('D', 'A')]

# for u, v in directed_edges:
#     graph_prac[u].append(v)

# for node in sorted(graph_prac.keys()):
#     print(sorted(graph_prac.get(node, [])))

# roads = [
#     ("Seoul", "Incheon"),
#     ("Seoul", "Daejeon"),
#     ("Daejeon", "Daegu"),
#     ("Daegu", "Busan"),
#     ("Incheon", "Suwon")
# ]
# from collections import defaultdict

# graph = defaultdict(list)

# for city1, city2 in roads:
#     graph[city1].append(city2)
#     graph[city2].append(city1)

# for city in graph:
#     print(graph[city1])

# visited = set()
# dfs_order = []

# def dfs_recursive(graph, node):
#     visited.add(node)
#     dfs_order.append(node)
#     for neighbor in graph.get(node, []):
#         if neighbor not in visited:
#             dfs_recursive(graph, neighbor)

# 그래프 정의
# graph = {
#     'A': ['B', 'D'],
#     'B': ['A', 'C', 'E'],
#     'C': ['B'],
#     'D': ['A', 'E'],
#     'E': ['B', 'D']
# }

# # 실행
# start_node = 'A'
# visited.clear()
# dfs_order.clear()

# if start_node in graph:
#     dfs_recursive(graph, start_node)
#     print(f"DFS 방문 순서: {dfs_order}")
# else:
#     print(f"시작 노드 '{start_node}'가 그래프에 없습니다.")

# lst = [5, 1, 4, 2, 3]
# # return_value = lst.sort(reverse=True)
# # print(return_value)
# # print(lst)

# new_lst = sorted(lst, reverse=True)
# print(new_lst)

# my_tuple = (5, 1, 4, 2, 3)
# sorted_tutple = sorted(my_tuple)
# print(sorted_tutple)


# words = ["banana", "apple", "kiwi", "strawberry", "orange"]
# print(f"원본 단어 리스트: {words}")

# sorted_len = sorted(words, key=len)
# print(sorted_len)
# print(words)

from collections import defaultdict

adj_lst = defaultdict(list)
edges = [(1, 2), (1, 0), (1, 3), (0, 3), (2, 3), (3, 4)]

for u, v in edges:
    adj_lst[u].append(v)
    adj_lst[v].append(u)

for node in sorted(adj_lst.keys()):
    print(sorted(adj_lst[node]))