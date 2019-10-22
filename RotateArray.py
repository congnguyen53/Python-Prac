
def rotationMat(arr):
    n = len(arr)
    n2 = len(arr[0])
    i = -1
    temp = [[ 0 for i in range(n2)] for j in range(n)]
    for x in range(n):
        n = len(arr)
        i += 1
        for y in range(n2):
            n -= 1
            temp[x][y] = arr[n][i]
    return temp


mat = [ [1, 2, 3 ],
        [4, 5, 6 ],
        [7, 8, 9 ] ]
rotationMat(mat)
print(rotationMat(mat))
