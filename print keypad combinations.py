hashtable = [' ', ' ', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
def keypad(number,curr,output,n):
    if curr==n:
        print(''.join(output), end=' ')
        return
    
    for i in range(len(hashtable[number[curr]])):
        output.append(hashtable[number[curr]][i])
        keypad(number,curr+1,output,n)
        output.pop()
        if (number[curr]==0 or number[curr]==1):
            return 
def printwords(number,n):
    keypad(number,0,[],n)

number=[2,3,4]
n=len(number)  
printwords(number,n)