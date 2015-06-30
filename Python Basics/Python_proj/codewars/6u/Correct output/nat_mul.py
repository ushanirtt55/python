def solution(number):
    """num=[]
    for i in range(1,number):
        if (i%3 == 0 or i%5 == 0):
            num.append(i)
    return sum(num)
"""
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
a=solution(10)
print a