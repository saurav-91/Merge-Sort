# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:07:30 2020

@author: SAURAV COOL
"""

def mergesort(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while(i<len(l)and j<len(r)):
            if(l[i]<r[j]):
                arr[k] = l[i]
                i = i+1
            else:
                arr[k] = r[j]
                j = j+1
            k = k+1
        while(i<len(l)):
                arr[k]=l[i]
                i=i+1
                k=k+1
        while(j<len(r)):
                arr[k]=r[j]
                j=j+1
                k=k+1
        return(arr)    

A = []
n = int(input("enter the number of elements:"))
for i in range(n):
    x = int(input("enter the value of element:"))
    A.append(x)
print(A) 
print("sorted Array")
#A.append(A[i])
print(mergesort(A))            