def BubbleSort(arr,n):
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1] :
                arr[j], arr[j+1]=arr[j+1], arr[j]
arr=list(map(int,input().split()))
n=len(arr)
print("Before Sorting:-",arr)
BubbleSort(arr,n)
print("after sorting :-", arr)