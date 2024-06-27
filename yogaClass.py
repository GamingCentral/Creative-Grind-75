#https://www.codechef.com/problems/YOGACLASS
#idea is to get max profit

# cook your dish here
case = int(input())
for i in range(case):
    n, x, y = [int(x) for x in input().split(' ')]
    y /= 2
    if n%2==0: #even hours then simple af
        if x>y:
            print(int(n*x)) 
        else:
            print(int(n*y))
    else:
        if x>y:
            print(int(n*x))
        else:
            print(int(((n-1)*y)+x))
    