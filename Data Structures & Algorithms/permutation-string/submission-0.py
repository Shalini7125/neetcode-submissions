class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r=0,len(s1)-1
        count={}
        if(len(s1)>len(s2)):
            return False
        for i in s1:
            count[i]=count.get(i,0)+1
        subcount={}
        for i in range(l,r+1):
            subcount[s2[i]]=subcount.get(s2[i],0)+1
        while(r<len(s2)):
            if({k: v for k, v in subcount.items() if v != 0}==count):
                return True
            else:
                subcount[s2[l]]=subcount.get(s2[l])-1
                l+=1
                r+=1
                if r < len(s2):
                    subcount[s2[r]]=subcount.get(s2[r],0)+1
        return False