"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
"""

def lists(a_lists):
    return[a_lists[0], a_lists[len(a_lists)-1]]

a = input("Enter any sequence of number: ")

print(a)
