#https://www.hackerrank.com/challenges/python-tuples

# Given an integer, n , and n space-separated integers as input, create a tuple, t, of those n integers. Then compute
# and print the result of hash(t).
#
# NOTE: You should solve this one in Python 2 (due to differences in the hash function between
# Python 2 and Python 3).  Also note that in python 2, you should use raw_input and not input.
#
# Example Input:
# 2
# 1 2
#
# Sample Output:
# 3713081631934410656

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())