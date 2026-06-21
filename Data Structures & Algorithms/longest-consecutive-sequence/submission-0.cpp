class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> a(nums.begin(),nums.end());
        int longest=0;
        for(int num:nums){
            if(a.find(num-1)==a.end()){
                int length=0;
                while(a.find(num+length)!=a.end()){
                    length++;

                }
                longest=max(longest,length);
            }
        }
        return longest;
        
    }
};
