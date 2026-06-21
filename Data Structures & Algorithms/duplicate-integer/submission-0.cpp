class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map <int,int> countmp;
        for(int i=0;i<nums.size();i++){
            if (countmp.find(nums[i])==countmp.end()){
                countmp[nums[i]]=1;
            }
            else{
                return true;
            }
        }

        return false;
    }
};