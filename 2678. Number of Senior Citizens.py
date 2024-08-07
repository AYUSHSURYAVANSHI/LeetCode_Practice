class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        counter = 0
        for i in details:
            if int(i[11:13]) > 60:
                counter+=1
        return counter