#idea is to get pairs of numbers that add up to be divisible by a given number
"""
https://www.codechef.com/problems/TREATS
"""

# cook your dish here
testcase = int(input())
for i in range(testcase):
    box, children = [int(x) for x in input().split(' ')]
    candies = [int(x) for x in input().split(' ')]
    chocolate = [int(x) for x in input().split(' ')]
    findChoco = {}
    findCandies = {}
    for i in candies:
        if (i%5) in findCandies:
            findCandies[i%5]+=1
        else:
            findCandies[i%5]=1
    for i in chocolate:
        if i%5 in findChoco:
            findChoco[i%5]+=1
        else:
            findChoco[i%5]=1
    count=0
    for key in findCandies:
        compliment = (children-key)%children
        if compliment in findChoco and key!=0:
            count+=(findChoco[children-key]*findCandies[key])
        if key==0 and key in findChoco:
            count+=(findChoco[key]*findCandies[key])
    print(count)
