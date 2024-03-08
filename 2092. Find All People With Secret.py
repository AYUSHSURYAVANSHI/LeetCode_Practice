<<<<<<< HEAD
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knw_st  = set([0, firstPerson])
        dct_frm = defaultdict(list)
        hpf     = []

        for psn_1, psn_2, time in meetings:
            dct_frm[psn_1].append((time, psn_2))   # psn_1 tell secret to psn_2 in time of the meeting
            dct_frm[psn_2].append((time, psn_1))   # psn_2 tell secret to psn_1 in time of the meeting

        if 0 in dct_frm:             hpf.extend(dct_frm[0])             # start from 0-person    
        if firstPerson in dct_frm:   hpf.extend(dct_frm[firstPerson])   # start from firstPerson  
        heapify(hpf)
        
        while hpf:  # in heap will be only people who know secret
                    # heap will return first (in time) spread of the secret 
                    # from person who already know the secret
            time, psn = heappop(hpf)
            
            if psn in knw_st:   continue   # person already know secret --> skip
            knw_st.add(psn)                # person doesn't know secret --> add to set
            
            # add to heap people who have meetings with current person 
            for (v_time, v_psn) in dct_frm[psn]: 
                if v_psn in knw_st:   continue   # person already know secret --> skip
                if v_time < time:     continue   # time of the next meeting before current time --> skip
                heappush(hpf, (v_time, v_psn))
        
=======
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knw_st  = set([0, firstPerson])
        dct_frm = defaultdict(list)
        hpf     = []

        for psn_1, psn_2, time in meetings:
            dct_frm[psn_1].append((time, psn_2))   # psn_1 tell secret to psn_2 in time of the meeting
            dct_frm[psn_2].append((time, psn_1))   # psn_2 tell secret to psn_1 in time of the meeting

        if 0 in dct_frm:             hpf.extend(dct_frm[0])             # start from 0-person    
        if firstPerson in dct_frm:   hpf.extend(dct_frm[firstPerson])   # start from firstPerson  
        heapify(hpf)
        
        while hpf:  # in heap will be only people who know secret
                    # heap will return first (in time) spread of the secret 
                    # from person who already know the secret
            time, psn = heappop(hpf)
            
            if psn in knw_st:   continue   # person already know secret --> skip
            knw_st.add(psn)                # person doesn't know secret --> add to set
            
            # add to heap people who have meetings with current person 
            for (v_time, v_psn) in dct_frm[psn]: 
                if v_psn in knw_st:   continue   # person already know secret --> skip
                if v_time < time:     continue   # time of the next meeting before current time --> skip
                heappush(hpf, (v_time, v_psn))
        
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return list(knw_st)