<<<<<<< HEAD
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
=======
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
>>>>>>> 45936108b93e7559b13be06f63781db262708cea
        return counter