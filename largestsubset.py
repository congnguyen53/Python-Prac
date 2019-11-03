'''
Given a set of distinct positive integers, find the largest subset such
that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example,
given the set [3, 5, 10, 20, 21],
you should return [5, 10, 20].
Given [1, 3, 6, 24], return [1, 3, 6, 24].
'''
def subset(arr):
    n = len(arr)
    arr1 = []
    arrhold = []

    for i in range(n):
        k=0
        for j in range(n):
            if(arr[i]%arr[j]==0 or arr[j]%arr[i]==0):
                k += 1
        arrhold.append(k)


    for i in range(n):
        if(arrhold[i]==max(arrhold)):
            arr1.append(arr[i])
    return arr1

arr = [3, 5, 10, 20, 21]
arr1 = [1, 3, 6, 24]
print(subset(arr))
print(subset(arr1))
