# """Adding numbers from 1 to 100 (Carl Gauss) """
#
#
# class Gauss:
#     def run(self):
#         name = self.__str__()
#         # sum(range(1, 101))
#         # (100 * (100 + 1))//2
#         _sum = 0
#         for i in range(101):
#             _sum += i
#         print(_sum)
#
#
# '''
# Valid anagram
#
# Given string S1 and S2 (iterable) check if two strings are anagram if they are made of the same frequencies.
# '''
#
#
# class ValidAnagram:
#     """ Checking anagram """
#
#     def __init__(self):
#         self.name = None
#
#     def using_hash_table(self, s1, s2):
#         self.name = self.__str__()
#         if not len(s1) == len(s2):
#             return False
#         hash_table_1 = {}  # S(n) = O(n)
#         hash_table_2 = {}  # S(n) = O(n)
#         # S_total = O(n)
#         for character in s1:  # T(n) = O(n)
#             if character in hash_table_1:
#                 hash_table_1[character] += 1
#             else:
#                 hash_table_1[character] = 1
#         for character in s2:  # T(n) = O(n)
#             if character in hash_table_2:
#                 hash_table_2[character] += 1
#             else:
#                 hash_table_2[character] = 1
#         for key in hash_table_1:  # T(n) = O(n)
#             if key not in hash_table_2 or hash_table_1[key] != hash_table_2[key]:
#                 return False
#         return True  # T_total(n) = O(n)
#
#     def using_counter_from_collections(self, s1, s2):
#         self.name = self.__str__()
#         from collections import Counter
#         if not len(s1) == len(s2):
#             return False
#         return Counter(s1) == Counter(s2)
#
#     def using_sorted(self, s1, s2):
#         self.name = self.__str__()
#         if not len(s1) == len(s2):
#             return False
#         return sorted(s1) == sorted(s2)  # T_total(n) = O(n log n)+ n(for ==) + O(n log n) = O(n log n)
#

'''
Given a sorted array of integers  arr and an integer target.
Find the index of the first and last position of target in arr.
If target cant be found in arr return [-1, -1]
e.g given arr =  [1, 2, 3, 4, 9, 9, 9, 9, 9, 9, 9, 10, 11, 13, 14, 15, 16, 17, 19] and target number is 9.
positions of 1st 9 is at index 4 and the last at index 10
program output to be [4, 10]
'''


class SortedArray:
    # This is a sorted array
    arr = [1, 2, 3, 4, 9, 9, 9, 9, 9, 9, 9, 10, 11, 13, 14, 15, 16, 17, 19]
    target = 9

    def using_traversing(self):
        """
            - T(n) = O(n) the worst case if there are no results we will traverse the whole array.\n
            - S(n) = O(1) since we are looping n variables space complexity will be constant
        """
        for i in range(len(self.arr)):
            if self.arr[i] == self.target:
                first_index = i
                while i + 1 < len(self.arr) and self.arr[i + 1] == self.target:
                    i += 1
                return [first_index, i]
        return [-1, -1]

    def using_binary_search(self):
        """
            DESCRIPTION\n
            - When using binary search; there is no searching specific position of target.
            - It's not ideal for this case because the list is sorted already.
            - find start function traverses the first half of the list/array and
            - find end function traverses the last half of the list/array
            TIME COMPLEXITY\n
            - T(n) = 2 * O(log n) = O(log n) since, we are using binary search twice
            - Time complexity here is a lot as we keep dividing input by 2
            - S(n) = O(1) since we are using eight variables
        """

        def find_start():
            # if element is on the first position return zero as index
            if self.arr[0] == self.target:
                return 0
            # set left and right to 0 and len(self.arr)-1
            # being the first position of the list and last respectively.
            left, right = 0, len(self.arr) - 1
            while left <= right:
                # mid-index as mid
                mid = (left + right) // 2
                print(mid, left, right)
                if self.arr[mid] == self.target and self.arr[mid - 1] < self.target:
                    # if mid is the target and if we move to the left the element is less than target,
                    # It means we found the first occurrence of the target.
                    break
                elif self.arr[mid] < self.target:
                    # if the position of mid is smaller than target it means we started far left.
                    # Increase left and try again inside the while loop
                    left = mid + 1

                else:
                    # otherwise it means we started far right where values are bigger than target.
                    # Therefore, we add right side.
                    right = mid + 1

            # On this portion of list we didn't find target.
            # Return -1 as default value
            return -1

        def find_end():
            print('find_end')
            if self.arr[-1] == self.target:
                return len(self.arr) - 1
            left, right = 0, len(self.arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if self.arr[mid] == self.target and self.arr[mid + 1] > self.target:
                    return mid
                elif self.arr[mid] > self.target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1


def find_start(arr, target):
    # if element is on the first position return zero as index
    if arr[0] == target:
        return 0
    # set left and right to 0 and len(self.arr)-1
    # being the first position of the list and last respectively.
    left, right = 0, len(arr) - 1
    while left <= right:
        # mid-index as mid
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid - 1] < target:
            # if mid is the target and if we move to the left the element is less than target,
            # It means we found the first occurrence of the target.
            return mid
        if arr[mid] < target:
            # if the position of mid is smaller than target it means we started far left.
            # Increase left and try again inside the while loop
            left = mid + 1
        # otherwise it means we started far right where values are bigger than target.
        # Therefore, we add right side.
        right = mid + 1
    # On this portion of list we didn't find target.
    # Return -1 as default value
    return -1


def find_end(arr, target):
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        left = mid + 1
    return -1


def start_and_end():
    arr = [1, 2, 3, 4, 9, 9, 9, 9, 9, 9, 9, 10, 11, 13, 14, 15, 16, 17, 19]
    target = 9
    # if array is empty, or first item in array is greater than target or
    # the last item of the array is less than target, return default list [-1, -1]
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    # start = find_start(arr, target)
    # end = find_end(arr, target)
    # return [start, end]


if __name__ == "__main__":
    print(start_and_end())
