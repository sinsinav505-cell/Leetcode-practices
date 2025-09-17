#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

l=[2,7,11,15]
l1=[]
l2=[]
for i in l:
    for j in l:
        if i+j==9:
            l1=(j,i)
            l2.append(l.index(j))
            l2.append(l.index(i))
        break
print(l2)