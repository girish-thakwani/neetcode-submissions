class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s2)<len(s1):
            return False
        d1=Counter(s1)
        l=0
        d2=Counter(s2[:len(s1)-1])
        print(d1,d2)
        for r in range(len(s1)-1,len(s2)):
            d2[s2[r]]=1+d2.get(s2[r],0)
            while l<=r and (d2[s2[r]]>d1[s2[r]] or s2[l] not in d1) :
                d2[s2[l]]-=1
                if d2[s2[l]]==0:
                    del d2[s2[l]]
                l+=1    
            print(d2)
            if d1==d2:
                return True
        return False          
        