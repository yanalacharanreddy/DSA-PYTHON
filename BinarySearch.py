#Binary Seacrh
#Time complexity of Function
# Best case  : O(1)
# Avg Case   : O(log(n))
# Worst Case : O(log(n))

def BinarySearch(arr,key,l,r):
    while(l<=r):
        mid=(l+r)//2
        if(key==arr[mid]):
            return "Key Found"
        elif key<arr[mid]:
            r=mid-1
        elif key>arr[mid]:
            l=mid+1
    return "Key Not Found"

arr=list(map(int,input().split()))
key=int(input())
arr.sort()
print(BinarySearch(arr,key,0,len(arr)-1))        
    