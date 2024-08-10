#find first and last occurence of element in string, using recursion
def solution(s, ele, index=0, first=-1, last=-1):
    if index==len(s):
        return first,last
    currchar=s[index]
    if currchar==ele:
        if first==-1:
            first=index
        last=index
    
    return solution(s,ele,index+1,first,last)
    
s = 'abababab'
sol = solution(s, 'b')
print(sol)
