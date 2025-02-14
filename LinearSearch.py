#Linear Search
# Time comlexity of Function
# Best case  : O(1)
# Avg Case   : O(N)
# Worst Case : O(N)

def LinearSearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return "Key Found"
    return "Key Not Found"

arr= list(map(int,input().split()))
key=int(input())

print(LinearSearch(arr,key))