# -*- coding: utf-8 -*-
"""Search_function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wh0jG187mWc-SwlvvJl3pDKGOr0VNF42
"""

# searching elements in an array 
# and print their indices...
# like where function 

def mysearch(arr, search_elem):
  arr_ind =[] 
  for i in range(len(arr)):
    if arr[i] == search_elem:
      arr_ind.append(i)
  print(arr_ind)

search_elem = 4
arr =[1, 2, 3, 4, 5, 4, 4]
print(arr)
mysearch(arr,search_elem)  # calling function and passing parameters
