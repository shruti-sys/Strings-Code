def solution(s,index=0,output='',seen=None):
    if seen is None:
        seen=set()
    if index==len(s):
        if output not in seen:
            print(output)
            seen.add(output)
        return    


    solution(s,index+1,output+s[index],seen)
    solution(s,index+1,output,seen)

s='aaa'
solution(s)