class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> indexmap;
        for(int i=0;i<nums.size();i++){
            int rem=target-nums[i];
            if (indexmap.find(rem)!=indexmap.end()){
                return {indexmap[rem],i};
            }
            else{
                indexmap[nums[i]]=i;
            }
        }
        
    }
};
