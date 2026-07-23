"""
need to understand monotonic stack first and its applications
increasing monotonic stack --> elements are stored in increasing order --> before pushing, pop all greater than the new element
decreasing monotonic stack --> elements are stored in decreasing order --> before pushing, pop all smaller than the new element

stacks solve problems (in O(n)) like: 
    next greater element
    next smaller element
    previous greater element
    previous smaller element

how?

"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                result[nums2[idx]] = nums2[i]
            stack.append(i)
        print(result)

        answer = []
        for j in range(len(nums1)):
            if nums1[j] in result:
                answer.append(result[nums1[j]])
            else:
                answer.append(-1)

        return answer
