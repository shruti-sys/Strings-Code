def sorted(arr,index=0):
    if index==len(arr)-1:
        return True
    if arr[index]>=arr[index+1]:
        return False
    return sorted(arr,index+1)


arr=[1,2,3,4,5,5]
print(sorted(arr))