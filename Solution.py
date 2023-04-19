def nextGreaterElement(nums1, nums2):
        map={n:i for i,n in enumerate(nums1)}
        result=[-1]*len(nums1)
        stack=[]
        for i in nums2:
            cur=i
            while stack and cur>stack[-1]:
                val=stack.pop()
                idx=map[val]
                result[idx]=cur
            if cur in map:
                stack.append(cur)
        return result
nums1=[4,1,3]
nums2=[1,3,2,4]
print(nextGreaterElement(nums1,nums2))
        
            