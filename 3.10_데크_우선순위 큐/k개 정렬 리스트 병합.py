import heapq

list1 = [1, 4, 5]
list2 = [1, 3, 4]
list3 = [2, 6]

# 리스트를 우선순위 큐로 변환
merged_list = heapq.merge(list1, list2, list3)

result = list(merged_list)
print(result)
