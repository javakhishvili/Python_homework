# მოცემულია რიცხვების სია [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
# გამოიყენეთ სორტირების ალორითმები: bubble sort, merge sort და insertion sort.
# შედეგები დაბეჭდეთ ეკრანზე.


# 1  bubble sort

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# numbers = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
# bubble_sort(numbers)
# print("Bubble Sort:", numbers)

# ---------------------------------------------------------------------

# 2  merge sort


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

# numbers = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
# merge_sort(numbers)
# print("Merge Sort:", numbers)



# -----------------------------------------------------------------------

# 3  insertion sort

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# numbers = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
# insertion_sort(numbers)
# print("Insertion Sort:", numbers)
