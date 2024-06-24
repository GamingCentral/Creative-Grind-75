#given an array then find indexes of elements which add up to given sum

class Solution:
    def targetedSum(self, arr, targetSum):
        for i in arr:
            if arr.index(targetSum-i):
                return [arr.index(i), arr.index(targetSum-i)]
        return -1
        
arr=[int(x) for x in input().split(' ')]
targetSum=int(input())
s=Solution()
l = s.targetedSum(arr, targetSum)
print(l)