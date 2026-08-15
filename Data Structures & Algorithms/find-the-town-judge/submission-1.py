class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people=set(i for i in range(1,n+1))
        for i in trust:
            if(i[0] in people):
                people.remove(i[0])

        candidate=next(iter(people)) if len(people) else -1
        people=set(i for i in range(1,n+1) if i!=candidate)
        for i in trust:
            if(i[1]==candidate and i[0] in people):
                people.remove(i[0])
        return candidate if(len(people))==0 else -1

        
        