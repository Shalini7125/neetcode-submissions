class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector <int> prefixsum(n);
        vector <int> suffixsum(n);
        prefixsum[0]=1;
        suffixsum[n-1]=1;
        for(int i=1;i<nums.size();i++){
            prefixsum[i]=nums[i-1]*prefixsum[i-1];
        }
        for(int i=n-2;i>=0;i--){
            suffixsum[i]=nums[i+1]*suffixsum[i+1];
        }
        vector <int> result(n);
        for(int i=0;i<n;i++){
            result[i]=prefixsum[i]*suffixsum[i];
        }
        return result;


    }
};
