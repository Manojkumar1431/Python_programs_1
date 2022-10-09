def sumoflarsmall(arr1, n):
    for i in range(1, n):
        lar = arr1[0]
        if arr1[i]>lar:
            lar=arr1[i];
        else:

