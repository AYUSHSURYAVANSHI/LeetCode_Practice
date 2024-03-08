<<<<<<< HEAD
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            d[tuple(count)].append(s)

=======
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            d[tuple(count)].append(s)

>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return d.values()