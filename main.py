def twoSum(nums, target):
    l=len(num)
    b_f=0
    ret=[]
    for i in range(0,l):
        for j in range(i+1,l):
            s=num[i]+num[j]
            if s==target:
                b_f=1
                ret.append(i)
                ret.append(j)
                break
        if b_f==1:
            break
            

    return ret
