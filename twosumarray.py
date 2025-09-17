#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

import numpy as np

l= np.array(list(map(int, input("Enter numbers").split())))
a=int(input("Enter the target:"))

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==a:
            print([i,j])