class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic=Counter(nums)
        list2=[]
        for i in range(max(dic.values())):
            list1=[]
            for key,freq in dic.items():
                if freq!=0:
                    dic[key]-=1
                    list1.append(key)
            list2.append(list1)
        return list2