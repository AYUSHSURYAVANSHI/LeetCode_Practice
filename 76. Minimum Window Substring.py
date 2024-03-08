<<<<<<< HEAD
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Define variables
        s_count, t_count = Counter(), Counter(t)
        
        l, r = 0, 0
        
        results = []
        
        while r <= len(s)-1:
                                    
            # Find valid window
            s_count[s[r]] += 1            
            r += 1
            if s_count & t_count != t_count:
                continue
                
            # Minimize this window
            while l < r:
                s_count[s[l]] -= 1 
                l += 1
                if s_count & t_count == t_count:
                    continue
                results.append(s[l-1:r])
                break
            
            
        # Return result
        if not results:
            return ""        
=======
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Define variables
        s_count, t_count = Counter(), Counter(t)
        
        l, r = 0, 0
        
        results = []
        
        while r <= len(s)-1:
                                    
            # Find valid window
            s_count[s[r]] += 1            
            r += 1
            if s_count & t_count != t_count:
                continue
                
            # Minimize this window
            while l < r:
                s_count[s[l]] -= 1 
                l += 1
                if s_count & t_count == t_count:
                    continue
                results.append(s[l-1:r])
                break
            
            
        # Return result
        if not results:
            return ""        
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return min(results, key=len)