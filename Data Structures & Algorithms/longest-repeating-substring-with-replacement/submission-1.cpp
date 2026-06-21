class Solution {
public:
    int characterReplacement(string s, int k) {
        map<char,int> count;
        int left=0;
        int n=s.length();
        int res=0;
        int maxf=0;
        for(int r=0;r<n;r++){
            count[s[r]]++;
            maxf=max(maxf,count[s[r]]);

            while((r-left+1-maxf)>k){
                
                count[s[left]]--;
                left++;
            }
            res=max(res,r-left+1);
        }
        return res;
        
    }
};
