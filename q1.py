def solution(n):
    if n==1 or n==0:
        return n
    else:
        for i in range(n):
            return solution(n-1)+solution(n-2)

n=10
sol=solution(n)
print(sol)
