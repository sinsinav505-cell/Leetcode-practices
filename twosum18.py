#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
import numpy as np

class Solution:

    def twoSum(self):
        x=input("Enter numbers: ")
        x=x.replace("["," ").replace("]"," ").replace(","," ")
        l= np.array(list(map(int, x.split())))

        a= input("Enter the target: ")
        a = a.replace("[", "").replace("]", "").replace(",", " ")
        a = list(map(int, a.split()))
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i]+l[j]==a:
                    print([i,j])

s=Solution()
s.twoSum()