def solution(s,index=0,output='',):
    
    if index==len(s):
        print(output)
        return
    solution(s,index+1,output+s[index])
    solution(s,index+1,output)

s='abc'
solution(s)
