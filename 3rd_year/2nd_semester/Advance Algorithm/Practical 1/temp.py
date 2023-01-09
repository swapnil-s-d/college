import time 
import random
import matplotlib.pyplot as plt

# get the start time
# st = time.time()

# wait for 3 seconds
# time.sleep(3)
# print('Sum of first 1 million numbers is:', sum_x)

# get the end time
# et = time.time()

# # get the execution time
# elapsed_time = et - st
# print('Execution time:', elapsed_time, 'seconds')


# Linear search O(n)----------------------------------------------------->

# arr = [] 
# x = []
# y = []
# for i in range(1000):
# 	# arr.append(random.randint(0,100))
# 	arr.append(i)

# for j in range (100):
# 	x.append(j)
# 	st = time.time()
# 	for k in range(1000):
# 		if arr[k]==j: break
# 	et = time.time()
# 	elapsed_time = et-st
# 	y.append(elapsed_time)

# plt.plot(x,y)
# plt.xlabel('Input size')
# plt.ylabel('Time')
# plt.title('Linear Search O(n)')
# plt.show()



# Sorting O(n^2)---------------------------------------------------------------->


# x = []
# y = []


# for k in range (100):
# 	x.append(k)
# 	arr = [] 
# 	for i in range(k):
# 		# arr.append(random.randint(0,100))
# 		arr.append(100-i)
# 	st = time.time()
# 	# Sorting code
# 	n = len(arr) 
# 	for i in range(n):
# 		for j in range(0, n - i - 1): 
# 			if arr[j] > arr[j + 1]:
# 				arr[j], arr[j + 1] = arr[j + 1], arr[j]
# 	et = time.time()
# 	elapsed_time = et-st
# 	y.append(elapsed_time) 

# plt.plot(x,y)
# plt.xlabel('Input size')
# plt.ylabel('Time')
# plt.title('Bubble Sort O(n^2)')
# plt.show()





# Merge Sort O(nlogn)---------------------------------------------------------------------------->

# def merge(left, right): 
#     if len(left) == 0:
#         return right
 
#     if len(right) == 0:
#         return left

#     result = []
#     index_left = index_right = 0 
#     while len(result) < len(left) + len(right): 
#         if left[index_left] <= right[index_right]:
#             result.append(left[index_left])
#             index_left += 1
#         else:
#             result.append(right[index_right])
#             index_right += 1 
#         if index_right == len(right):
#             result += left[index_left:]
#             break

#         if index_left == len(left):
#             result += right[index_right:]
#             break

#     return result


# def merge_sort(array): 
#     if len(array) < 2:
#         return array

#     midpoint = len(array) // 2
 
#     return merge(
#         left=merge_sort(array[:midpoint]),
#         right=merge_sort(array[midpoint:]))



# x = []
# y = []


# for k in range (100):
# 	x.append(k)
# 	arr = [] 
# 	for i in range(k):
# 		# arr.append(random.randint(0,100))
# 		arr.append(100-i)
# 	st = time.time()
# 	# Sorting 
# 	merge_sort(arr)
# 	et = time.time()
# 	elapsed_time = et-st
# 	y.append(elapsed_time) 

# plt.plot(x,y)
# plt.xlabel('Input size')
# plt.ylabel('Time')
# plt.title('Merge Sort O(nlogn)')
# plt.show()



# Binary Search O(logn) --------------------------------------------->


# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
 
#     while low <= high:
 
#         mid = (high + low) // 2
 
#         if arr[mid] < x:
#             low = mid + 1
 
#         elif arr[mid] > x:
#             high = mid - 1
 
#         else:
#             return mid
 
#     return -1
 



# arr = [] 
# x = []
# y = []
# for i in range(1000):
# 	# arr.append(random.randint(0,100))
# 	arr.append(i)

# for j in range (100):
# 	x.append(j)
# 	st = time.time()
# 	binary_search(arr,j)
# 	et = time.time()
# 	elapsed_time = et-st
# 	y.append(elapsed_time)

# plt.plot(x,y)
# plt.xlabel('Input size')
# plt.ylabel('Time')
# plt.title('Binary Search O(logn)')
# plt.show()



# O(n^3)--------------------------------------------------->


arr=[]
x = []
y = []
for i in range(10): 
	arr3 = []
	for j in range(i):
		arr3.append(j)
	arr.append(arr3)

x.append(i)
st = time.time()
binary_search(arr,j)
et = time.time()
elapsed_time = et-st
y.append(elapsed_time)
 

plt.plot(x,y)
plt.xlabel('Input size')
plt.ylabel('Time')
plt.title('Binary Search O(logn)')
plt.show()